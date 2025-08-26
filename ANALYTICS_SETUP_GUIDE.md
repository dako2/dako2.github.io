# Web Analytics Setup Guide

This guide explains how to set up Google Analytics tracking for your personal website.

## Google Analytics 4 (GA4) Setup

### Step 1: Create Google Analytics Account
1. Go to [Google Analytics](https://analytics.google.com/)
2. Sign in with your Google account
3. Click "Start measuring" to create a new account
4. Follow the setup wizard to create a property for your website

### Step 2: Get Your Measurement ID
1. In your GA4 property, go to Admin (gear icon)
2. Under "Property", click "Data Streams"
3. Click on your web stream
4. Copy your "Measurement ID" (format: G-XXXXXXXXXX)

### Step 3: Update Your Website
1. Replace `GA_MEASUREMENT_ID` in all HTML files with your actual Measurement ID
2. The tracking code is already installed in:
   - `index.html` (main page)
   - `blog.html` (blog page)
   - `photos.html` (photo gallery)

### Step 4: Verify Tracking
1. Deploy your changes to GitHub Pages
2. Visit your website in a browser
3. In Google Analytics, go to Reports > Realtime
4. You should see your visit appear within a few minutes

## What Gets Tracked

The current implementation tracks:
- **Page views** - Every time someone visits a page
- **User sessions** - How long visitors stay on your site
- **Traffic sources** - Where visitors come from (search, direct, referral)
- **Geographic data** - General location of visitors (country/region)
- **Device information** - Desktop vs mobile usage

## Privacy Considerations

- Google Analytics complies with GDPR and other privacy regulations
- No personally identifiable information is collected
- Users can opt out using browser settings or extensions
- Consider adding a privacy policy to your website

## Alternative Analytics Options

If you prefer alternatives to Google Analytics:
- **Plausible** - Privacy-focused, lightweight
- **Fathom** - Simple, privacy-first analytics
- **Umami** - Open-source, self-hosted option
- **Simple Analytics** - GDPR-compliant alternative

## Troubleshooting

### Common Issues:
1. **No data showing**: Wait 24-48 hours for data to appear
2. **Tracking not working**: Check browser console for JavaScript errors
3. **Wrong Measurement ID**: Verify the ID format (G-XXXXXXXXXX)

### Testing:
- Use Google Analytics Debugger browser extension
- Check Network tab in browser dev tools for gtag requests
- Use Google Tag Assistant for validation

## File Locations

Analytics tracking code has been added to:
```
/index.html (lines 9-15)
/blog.html (lines 9-15)  
/photos.html (lines 9-15)
```

Replace `GA_MEASUREMENT_ID` with your actual tracking ID in all three files.
