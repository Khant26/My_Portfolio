# Design QA

References:
- Selected Minimal Technical portfolio direction
- User-supplied architectural portrait used as the identity reference
- User-supplied hero, contact, and CV screenshots

Implementation: index.html and Khant_Maung_CV.pdf
Viewports reviewed: 1536 x 1024 desktop and 390 x 844 mobile

## Hero

- Replaced the framed architectural photograph with a transparent professional head-and-shoulders cutout derived from the user-supplied portrait.
- Preserves Khant Maung's face, round glasses, hairstyle, skin tone, and white shirt while removing the entire background.
- Rebalanced the portrait to a 460 x 356 px desktop frame and a centered 300 x 260 px mobile frame.
- Shifted the desktop portrait closer to the headline and slightly lower for stronger visual alignment; tightened the mobile hero gap.
- Uses real PNG alpha transparency with refined hair, glasses, shoulder, and shirt edges; the portrait blends directly into the black hero background.
- Rebuilt the hero portrait from the original university photograph as the sole facial-form reference, prioritizing the same narrow oval face, jaw, eyes, nose, lips, glasses, hairstyle, skin tone, age, and slim proportions.
- Removed the "Khant Maung / 2026" portrait caption.
- Includes a continuously moving technology ticker with 20 verified languages, frameworks, databases, delivery tools, and QA technologies.
- Ticker pauses on hover and becomes static when reduced motion is enabled.
- Desktop and mobile checks show zero horizontal overflow, one successfully loaded hero image, and zero console errors.

## Layout and functionality

- Contact follows the supplied structured reference with direct methods, quick facts, and a focused email call to action.
- Contact height was reduced to 703 px on desktop and 1040 px on mobile using tighter section padding, smaller cards, shorter contact rows, a slimmer banner, and a two-column mobile phone/GitHub row.
- Navigation order is Experience, Work, Skills, Contact; every link targets its heading, fits on one line at 390 px, clears the sticky header, and receives an active-section underline.
- The hero View Work button also targets the Work heading; four selectable project rows, contact links, external links, and CV download remain functional.
- Work-section whitespace is tightened to 61/40/62 px (top/title gap/bottom) on desktop and 40/24/41 px on mobile.
- Local page, portrait, CV, robots.txt, and sitemap.xml return successful responses.

## CV

- CV remains a one-page portfolio-matched PDF.
- "Junior" and "Mid Level" wording is removed.
- PDF is readable, unencrypted, text-selectable, and contains working hyperlinks.
- Final render has no clipping, overlap, missing glyphs, or broken images.

final result: passed

## Theme modes

- Defaults to the browser or operating-system color preference through prefers-color-scheme.
- Provides a keyboard-accessible manual light/dark toggle with a saved local preference.
- Light mode uses dedicated background, surface, text, muted-text, border, accent, and header colors rather than color inversion.
- Browser theme-color metadata updates with the active mode.
- Mobile navigation spacing was tightened to accommodate the theme control.

## Revised CV

- CV now uses the exact transparent portrait used by the portfolio hero.
- Visual language matches the portfolio: near-black header, lime accent, monospace section labels, warm neutral surfaces, and restrained dividers.
- Added engineering-practice and availability detail without inventing metrics or responsibilities.
- Preserved email, phone, GitHub, portfolio, and LinkedIn hyperlinks.
- CV remains one A4 page with all text and links inside page bounds.
- CV assets, editable generator, finished PDF, and previous-version archive are organized under myCV.
