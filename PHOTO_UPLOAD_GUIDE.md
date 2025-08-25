# Photo Upload Guide

## Standardized Format for Adding New Photos

This guide explains how to add new photos to the photo gallery while maintaining the Instagram-style collage layout.

### Image Requirements

**File Format:** JPG or PNG  
**Recommended Size:** 800x800px minimum (square aspect ratio works best)  
**File Naming:** Use descriptive, URL-friendly names with underscores  
**Location:** Save images in `/images/` directory

### Adding a New Photo

1. **Save the image file** to `/images/` directory with a descriptive name:
   ```
   /images/your_descriptive_filename.jpg
   ```

2. **Edit photos.html** and add a new photo item in the `.photo-grid` div:
   ```html
   <div class="photo-item">
     <img src="/images/your_descriptive_filename.jpg" alt="Descriptive alt text">
     <div class="photo-caption">
       <strong>Photo Title</strong><br>
       Brief description of the photo, event, or context. Keep it concise but informative.
     </div>
   </div>
   ```

### Photo Caption Format

**Title:** Use `<strong>` tags for the main title  
**Description:** Add context, location, date, or significance  
**Length:** Keep descriptions to 1-2 sentences for clean layout

### Example Photo Entry

```html
<div class="photo-item">
  <img src="/images/conference_speaker_2024.jpg" alt="Speaking at Tech Conference 2024">
  <div class="photo-caption">
    <strong>Tech Conference Keynote (2024)</strong><br>
    Presenting research on AI hardware acceleration at the International Tech Conference in San Francisco.
  </div>
</div>
```

### CSS Styling (Automatic)

The Instagram-style layout automatically applies:
- ✅ Rounded corners (12px)
- ✅ Hover effects with subtle lift
- ✅ Consistent 280px height
- ✅ Clean white backgrounds
- ✅ Modern box shadows
- ✅ Responsive grid layout

### File Naming Examples

Good naming conventions:
- `team_photo_2024.jpg`
- `conference_keynote_sf.jpg`
- `research_lab_visit.jpg`
- `industry_meetup_nyc.jpg`

Avoid:
- Spaces in filenames
- Special characters
- Very long names
- Generic names like `photo1.jpg`

### Testing

After adding a new photo:
1. Check that the image loads correctly
2. Verify the caption displays properly
3. Test on mobile devices for responsive layout
4. Ensure the Instagram-style hover effects work

The photo gallery maintains the engineering arts aesthetic while providing a modern, Instagram-like collage experience.
