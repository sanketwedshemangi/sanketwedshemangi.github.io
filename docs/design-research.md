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
