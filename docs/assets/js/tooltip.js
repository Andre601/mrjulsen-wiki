/**
 * Creates Minecraft-style tooltips
 *
 * Replaces normal tooltips.
 * Supports HTML-style MiniMessage tags, including <yellow>, <bold>, and custom colors like <#abcdef>.
 *
 * Old color codes and corresponding MiniMessage tags:
 *
 * &0 = <black>      &1 = <dark_blue>      &2 = <dark_green>  &3 = <dark_aqua>
 * &4 = <dark_red>   &5 = <dark_purple>    &6 = <gold>        &7 = <gray>
 * &8 = <dark_gray>  &9 = <blue>           &a = <green>       &b = <aqua>
 * &c = <red>        &d = <light_purple>   &e = <yellow>      &f = <white>
 *
 * &l = <bold>       &m = <strikethrough>  &n = <underline>   &o = <italic>
 * &r = <reset>
 */
(function() {
	'use strict';

	document.addEventListener('DOMContentLoaded', function() {
		const contentText = document.body;

		if (!contentText) return;

		const escapeHTML = (str) =>
				str.replace(/[&<>"]/g, (m) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[m]));

		const parseMiniMessage = (text) => {
			const colorMappings = {
				black: "#000000",
				dark_blue: "#0000A8",
				dark_green: "#00A800",
				dark_aqua: "#00A8A8",
				dark_red: "#A80000",
				dark_purple: "#A800A8",
				gold: "#FBA800",
				gray: "#A8A8A8",
				dark_gray: "#545454",
				blue: "#5454FB",
				green: "#54FB54",
				aqua: "#54FBFB",
				red: "#FB5454",
				light_purple: "#FB54FB",
				yellow: "#FBFB54",
				white: "#FBFBFB",
				trim_quartz: "#E3D4C4",
				trim_iron: "#ECECEC",
				trim_netherite: "#625859",
				trim_redstone: "#971607",
				trim_copper: "#B4684D",
				trim_gold: "#DEB12D",
				trim_emerald: "#11A036",
				trim_diamond: "#6EECD2",
				trim_lapis: "#416E97",
				trim_amethyst: "#9A5CC6",
				trim_resin: "#FC7812",
			};

			const openTags = [];
			const html = [];

			const closeOpenTags = () => {
				while (openTags.length > 0) {
					openTags.pop();
					html.push(`</span>`);
				}
			};

			text.split(/(<[^>]+>)/g).forEach((segment) => {
				if (!segment) return;

				if (segment.startsWith("<") && segment.endsWith(">")) {
					let tag = segment.slice(1, -1);
					const customColor = tag.match(/^#([0-9a-fA-F]{3,6})$/);

					if (tag === 'br') {
						closeOpenTags();
						html.push('<br>');
					} else if (tag === 'reset') {
						closeOpenTags();
					} else if (tag.startsWith("/")) {
						const closingTag = tag.slice(1);
						const lastOpenTag = openTags[openTags.length - 1];
						if (lastOpenTag && (lastOpenTag === closingTag || customColor)) {
							openTags.pop();
							html.push(`</span>`);
						}
					} else if (tag.startsWith("!")) {
						// Simply do nothing and return
					} else if (customColor) {
						openTags.push(tag);
						html.push(`<span style="color: #${customColor[1]};">`);
					} else if (tag in colorMappings) {
						openTags.push(tag);
						html.push(`<span style="color: ${colorMappings[tag]};">`);
					} else {
						openTags.push(tag);
						html.push(`<span class="format-${tag}">`);
					}
				} else {
					html.push(escapeHTML(segment));
				}
			});

			closeOpenTags();

			return html.join("").replaceAll('&amp;lt;', '&lt;').replaceAll('&amp;gt;', '&gt;');
		};

		let tooltip = null;
		const win = window;

		const removeTooltip = () => {
			if (tooltip) {
				tooltip.remove();
				tooltip = null;
			}
		};

		contentText.addEventListener('mouseenter', function(e) {
			const target = e.target.closest('.invslot-item, .shapeless');
			if (!target || !target.hasChildNodes()) return;

			removeTooltip();

			let title = target.dataset.minetipTitle;
			if (title === undefined) {
				title = target.getAttribute('title');
				if (title !== null) {
					title = title.trim();
					target.dataset.minetipTitle = title;
				}
			}

			if (!title || title.replace(/<[^>]+>/g, '').trim() === '') {
				title = "<red><bold>ERROR: No title specified";
			}

			let content = `<span class="minetip-title">${parseMiniMessage(title)}</span>`;

			let description = target.dataset.minetipText;
			if (description) {
				const attributes = {
					"<final>": "<gold><bold><underline>Final<reset><italic> (Can not be modified or repaired)",
					"<fragile>": "<gold><bold><underline>Fragile<reset><italic> (Damaged on Death)",
					"<games only>": "<gold><bold><underline>Games Only<reset><italic>(For Games server only. Cannot /vault or /mail<dark_purple>)",
					"<replaceable>": "<gold><bold><underline>Replaceable<reset><italic> (Can be placed every 6 hours)",
					"<soulbound>": "<gold><bold><underline>Soulbound<reset><italic> (Will not drop on death)",
					"<temporary>": "<gold><bold><underline>Temporary<reset><italic> (Time Limited Items)",
					"<unbreakable>": "<gold><bold><underline>Unbreakable",
					"<unplaceable>": "<gold><bold><underline>Unplaceable<reset><italic> (Can not be placed)",
					"<unusable>": "<gold><bold><underline>Unusable<reset><italic> (Can not be used)",
					"<voting reward>": "<gold><bold><underline>Voting Reward",
					"<wearable>": "<gold><bold><underline>Wearable<reset><italic> (Right click to Equip)",
					"<do not claim>": "<red>&lt;&lt;&lt; DO NOT CLAIM : CLAIM CHEST ABOVE &gt;&gt;&gt;",
				};
				for (const key in attributes) {
					description = description.replaceAll(key, attributes[key])
				}

				const escapedDescription = parseMiniMessage(description.replace(/\n/g, '<br>'));

				content += `<span class="minetip-description">${escapedDescription}</span>`;
			}

			tooltip = document.createElement('div');
			tooltip.id = 'minetip-tooltip';
			tooltip.innerHTML = content;
			document.body.appendChild(tooltip);

			const tooltipWidth = tooltip.offsetWidth;
			const tooltipHeight = tooltip.offsetHeight;

			let left = e.clientX + 10;
			let top = e.clientY - 30;

			if (left + tooltipWidth > win.innerWidth) {
				left -= tooltipWidth + 24;
			}
			if (top + tooltipHeight > win.innerHeight) {
				top -= tooltipHeight - 18;
			}

			tooltip.style.left = `${Math.max(left, 0)}px`;
			tooltip.style.top = `${Math.max(top, 0)}px`;
		}, true);

		contentText.addEventListener('mouseleave', function(e) {
			const target = e.target.closest('.invslot-item, .shapeless');
			if (!target) return;

			removeTooltip();
		}, true);

		contentText.addEventListener('mousemove', function(e) {
			if (!tooltip) return;

			const rect = tooltip.getBoundingClientRect();
			let left = e.clientX + 10;
			let top = e.clientY - 30;

			if (left + rect.width > win.innerWidth) {
				left -= rect.width + 24;
			}
			if (top + rect.height > win.innerHeight) {
				top -= rect.height - 18;
			}

			tooltip.style.left = `${Math.max(left, 0)}px`;
			tooltip.style.top = `${Math.max(top, 0)}px`;
		}, true);

		const images = contentText.querySelectorAll('.invslot-item img');
		images.forEach((img) => {
			const parent = img.closest('.invslot-item');
			if (parent) {
				const title = parent.dataset.minetipTitle;
				if (title) {
					img.alt = title.replace(/<[^>]+>/g, '').trim();
				}
			}
		});
	});
})();
