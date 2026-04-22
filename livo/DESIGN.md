# LIVO Design System: The Digital Curator

## 1. Overview & Creative North Star
**LIVO** is a premium, editorial-style platform designed to bridge the gap between housing utility and lifestyle inspiration. The platform serves as a curated marketplace for finding roommates, house shares, and domestic services (vendors and house help).

The Creative North Star for LIVO is **"The Digital Curator."** 
Moving beyond typical SaaS layouts, LIVO treats every listing as a high-end editorial feature. The interface reflects the sophistication of a lifestyle magazine while maintaining the functional precision of a modern financial tool.

---

## 2. Visual Language

### 2.1 Color Palette: Tonal Sophistication
LIVO utilizes a palette that emphasizes depth through subtle shifts rather than harsh lines.

- **Primary (LIVO Red):** `#BA0036` (Primary) and `#8E0027` (Deep). Used as an authoritative accent for high-impact actions and brand identity.
- **Surface & Foundation:** `#F9F9F9`. A gallery-style off-white canvas that reduces eye strain and establishes a premium environment.
- **Typography & Slate:** `#1A1C1C`. A deep charcoal used for editorial-grade readability.

#### The "No-Line" Rule
*   **Boundaries through Background Shifts:** Sectional separation is achieved by placing a `surface-container-low` component on a `surface` background.
*   **Negative Space:** The 8px grid is leveraged to create clear, breathable voids between content clusters. 1px solid borders are strictly avoided for sectioning.

### 2.2 Design Tokens (CSS Variables)
To implement the LIVO aesthetic, use the following tokens in your base stylesheet:

```css
:root {
  /* Brand Colors */
  --livo-red: #BA0036;
  --livo-red-deep: #8E0027;
  --livo-red-container: #E21E4A;
  
  /* Surfaces */
  --surface: #F9F9F9;
  --surface-low: #F3F3F3;
  --surface-lowest: #FFFFFF;
  --surface-high: #E8E8E8;
  --surface-highest: #E2E2E2;
  
  /* Typography */
  --on-surface: #1A1C1C;
  --secondary: #5F5E5E;
  --outline-variant: rgba(229, 189, 190, 0.2); /* Ghost Border */
  
  /* Rounding */
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;
  
  /* Spacing */
  --spacing-unit: 8px;
}
```

### 2.3 Typography: Editorial Authority
LIVO employs a dual-font strategy to balance professional engineering with lifestyle personality.

- **Headlines (Manrope):** Geometric and confident. Features tight `-2%` tracking for a "premium print" look.
- **Body & UI (Inter):** The workhorse for readability. Leans into extreme weight contrasts (300 for captions, 600 for titles) to establish drama and hierarchy.
- **Micro-Copy:** Uppercase labels with `0.05em` letter-spacing for a technical, precise "metadata" aesthetic.

### 2.4 Elevation & Depth: Tonal Layering
Depth is achieved through **Surface Nesting** rather than traditional heavy shadows.

1.  **Base:** `surface` (#F9F9F9)
2.  **Section:** `surface_container_low` (#F3F3F3)
3.  **Component:** `surface_container_lowest` (#FFFFFF)

By stacking lighter containers on darker backgrounds, we create a "lift" effect that feels architectural and airy.

---

## 3. Component Architecture

### 3.1 Buttons
- **Primary:** High-gloss gradient from `#BA0036` to `#E21E4A`. Features `xl` (1.5rem) or `full` roundedness.
- **Secondary:** Transparent background with a "Ghost Border" (15-20% opacity `outline-variant`).
- **Tertiary:** Text-only in `primary` color with heavy weight for editorial momentum.

### 3.2 Cards & Feed Items
- **Structure:** Edge-to-edge imagery with generous padding (24px) for metadata.
- **Rounding:** `xl` (24px) or `lg` (16px) corners to emphasize softness and invitation.
- **Interaction:** No divider lines; cards are separated by vertical whitespace (32px - 48px).

### 3.3 Input Fields
Minimalist execution using `surface-container-low` as a subtle background fill. On focus, the field transitions to `surface-container-lowest` with a 1px "Ghost Border" in LIVO Red.

---

## 4. Layout Principles

### 4.1 Editorial Asymmetry
To break the "grid-prison," LIVO uses intentional asymmetry in hero sections and profile views. Elements like profile photos or badges may overlap containers to create a sense of bespoke craftsmanship.

### 4.2 Glassmorphism
Floating elements, such as sticky headers and mobile navigation, utilize semi-transparent versions of `surface` colors with a `backdrop-blur` of 12px–20px.

---

## 5. Project Information

### User Roles
The LIVO ecosystem supports four distinct user experiences:
1.  **Roommate:** Social-first feed for finding house shares and lifestyle matches.
2.  **House Owner:** Portfolio-focused dashboard for property management.
3.  **Vendor:** Meal and service management for domestic providers.
4.  **Househelp:** Review-centric dashboard for domestic professionals.

### Primary Screens
- **Landing Page:** Showcasing updated features and lifestyle branding.
- **Roommate Feed:** Social discovery platform.
- **Dashboards:** Tailored management views for all four user roles.
- **Social Detail Views:** High-impact "gallery" views for specific listings.
- **Onboarding:** Editorial-focused Login and Signup experiences.

---

## 6. Do’s and Don’ts

### Do
- **Do** use extreme vertical white space.
- **Do** lean on typographic scale rather than bolding for hierarchy.
- **Do** treat imagery with the reverence of a museum exhibit.

### Don't
- **Don't** use 1px solid black or grey borders.
- **Don't** use standard Material Design drop shadows.
- **Don't** use pure black (#000000); always use the `#1A1C1C` charcoal.
