# Design research: professional digital wedding invitations

Researched 2026-11-12 to guide the redesign of `src/site.template.html`. Several vendor sites (Greenvelope, David's Bridal, withjoy) block automated fetches, so some points come from their search snippets or from competitor/industry write-ups. Each bullet ends with what it changed here.

## Typography

- **Names are the single focal point; everything else steps down in 2-3 sizes.** Hierarchy goes names, then date/time/venue, then minor details, built with size, weight and spacing rather than more typefaces. Sources: https://madegooddesigns.com/invitation-design-guide/ , https://text.design/text-design-resources/typography-in-wedding-invitations , https://paperlust.co/blog/wedding-invitation-fonts/
  -> Script is now used only for the couple's names (hero, envelope, signature). All headings moved from script to a serif.
- **Two families max; script used sparingly because it hurts readability.** Classic pairing is a calligraphic script plus a Garamond-style serif. Source: https://text.design/text-design-resources/typography-in-wedding-invitations
  -> Dropped Great Vibes and Cinzel. Now Pinyon Script (names) + Cormorant Garamond (everything else), plus Tiro Devanagari Marathi for the two chants.
- **Short all-caps lines get opened tracking for an engraved look; never set long details in caps.** Source: https://madegooddesigns.com/invitation-design-guide/ , https://paperlust.co/blog/wedding-invitation-fonts/
  -> Kickers ("Save the date", "Join us", day/date lines, family labels) are 11-12px caps at 0.22-0.32em tracking. Addresses and times stay in sentence case.
- **Paid Indian website-invite services standardise on the same pairing.** zareqia.com loads Cormorant Garamond, Cinzel, Great Vibes, Allura, Italianno; bridy (https://bridy-ct2.pages.dev/) loads Pinyon Script + Allura + Cormorant Garamond. Source: page HTML of https://zareqia.com and https://bridy-ct2.pages.dev/
  -> Confirms Cormorant as the workhorse; Pinyon Script chosen as the finer, more "engraved" script.
- **Script ampersands are often illegible.** Pinyon's `&` read as a stray squiggle in our render. Stationers commonly set the ampersand in an italic serif as a deliberate accent. Source: https://madegooddesigns.com/invitation-design-guide/ (third face "only as a sparing accent such as an ampersand")
  -> Every ampersand between the names (envelope, seal, hero, signature) is Cormorant italic.

## Spacing, ornament, colour

- **"Restraint reads as luxury." Crowding is the most common amateur tell; pick one accent, not several.** Source: https://madegooddesigns.com/invitation-design-guide/ ; also the luxury wedding site guidance summarised at https://www.davidsbridal.com/content/luxury-wedding/designing-digital-elegance-the-luxury-wedding-website-manifesto (information overload is the top mistake)
  -> Removed the heart ornaments. One ornament system everywhere: a small gold dharma wheel between hairlines, which also carries the Buddhist identity. A plain gold hairline separates the two events.
- **Shared margins and a shared grid make a suite read as one set.** Source: https://madegooddesigns.com/invitation-design-guide/ , https://premium-wedding-invites.pages.dev/blog/top-10-wedding-invitation-trends-2026 ("cohesive design systems")
  -> Every card has the same padding (52/26/48px), the same kicker > heading > content rhythm, and a gold inset hairline frame like a printed card edge.
- **Two inks plus paper.** Source: https://madegooddesigns.com/invitation-design-guide/
  -> Text is plum ink only; gold is reserved for ornaments, icons and hairlines. The lavender frosted glass stays as the "paper".

## Opening reveal and structure

- **The envelope reveal is the signature moment, but it must be light and mobile-first** (Paperless Post moved to a lighter, single-page animation after a heavy one hurt mobile engagement; 55% of invitations are opened on phones). Source: https://invisionapp.com/inside-design/paperless-post (via search summary; page now redirects), Greenvelope comparison https://lasoireechicevents.greenvelope.com/compare/greenvelope-vs-paperless-post
  -> Kept the wax-seal envelope; replaced the blinking "Tap to open" with a soft halo pulse on the seal and steady text. On short screens (<=720px tall) the flap and seal sit higher so "Tap to open" never crowds the names.
- **Market standard for Indian website invites: envelope intro, music on open, countdown, events with map links, families.** Sources: https://zareqia.com (scratch card date reveal, curtain animations, countdown), https://bridy-ct2.pages.dev/ , https://contra.com/p/eBA3EYZe-share-my-invite-digital-wedding-invitation-platform-development , https://premium-wedding-invites.pages.dev/blog/top-10-wedding-invitation-trends-2026
  -> Flow unchanged (captain's decisions), content unchanged.
- **Hero should hint, not tell everything; names or a short greeting lead.** Source: https://www.zola.com/expert-advice/wedding-website-examples-and-inspiration-themes-and-designs
  -> Hero keeps names and parents only; the date stays hidden for the scratch reveal.

## Components

- **Countdown:** premium templates use quiet numerals with small caps units rather than heavy badges (Zola/Framer templates such as https://www.framer.com/marketplace/templates/together-vows/ ).
  -> Light Cormorant lining numerals, tabular widths, gold hairline dividers instead of circles.
- **Buttons:** amateur sites use heavy filled buttons; refined ones use outlined, tracked, small-caps labels with comfortable tap targets.
  -> "View on Google Maps" is a 46px-tall outlined pill with a pin icon and tracked caps.
- **Venue cards:** group date with time and venue with address. Source: https://madegooddesigns.com/invitation-design-guide/
  -> Each event: icon, title, caps day/date, italic time, address (balanced wrap), button.
- **Numerals:** Cormorant's default old-style figures make dates look uneven; lining numerals read as more formal on screens.
  -> `font-variant-numeric: lining-nums` across the page.

## 2026-11-12 rebuild: no drawn art

The captain found the code-drawn art (leaf-pattern envelope, sunset arch with roses, curtains, petals) amateur and asked for a frontend-design build instead of illustrations or sourced watercolour assets. The page now uses no images at all; everything is paper, glass, light and type in CSS/SVG.

- **Envelope:** a pearl-lavender envelope on the twilight sky. Its panels are lit separately (gradients per fold, a soft flap shadow, SVG `feTurbulence` paper grain) so it reads as real stock. The gold wax seal uses SVG lighting filters (displaced edge, specular dome, debossed S&H monogram) rather than flat fills.
- **Opening:** one orchestrated sequence, all CSS transitions on a single `.open` class so it is seekable: seal lifts (0-0.55s), flap turns over in 3D (0.25-1.25s), the card rises (1.05-2.05s), the envelope fades into the hero (2.05-2.95s), then the arch and its lines settle in (2.15-4.3s). Reduced motion skips it.
- **Hero:** a luminous glass arch (backdrop blur, gold inset hairline) on the same twilight gradient, so the envelope dissolves into it with no seam.
- **Sheet:** one frosted sheet with an arched top replaces five identical cards (the "SaaS card kit" tell). Per-section fade-ins were removed so the page is complete at rest.
- **Type:** the tracked all-caps eyebrows were replaced with small italic kickers and sentence-case units/buttons; frontend-design guidance flags caps labels as a templated tell. Allura stays for the names only.
- **Date reveal:** the scratch heart became a frosted glass pane you wipe clear (canvas, soft brush), matching the glass language.
- **Events:** each event is anchored by its large day numeral with details left-aligned beside it, instead of a drawn icon.

Screenshots: `docs/screenshots/before-*` (the previous live design) and `after-*` (this rebuild), at 360x640, 390x844, 430x932 and 1440x900; closed, mid-opening and opened.
