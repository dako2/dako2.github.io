# Blog Upload Guide

## Standardized Format for Adding New Blog Posts

This guide explains how to add new blog posts to maintain consistent formatting and structure while preserving the engineering arts aesthetic.

### Blog Post Structure

Each blog post should follow this standardized HTML structure in `blog.html`:

```html
<article>
<h3>Blog Post Title</h3>
<p><i>Date (Month DD, YYYY)</i></p>

<!-- Optional: Brief introduction paragraph -->
<p>Brief introduction or summary of the blog post content.</p>

<!-- Main content with sections -->
<h4>Section Title</h4>
<ul>
<li><b>Key Point:</b> Description or explanation</li>
<li><b>Another Point:</b> More details with <a href="URL">relevant links</a></li>
</ul>

<h4 id="section-anchor">Another Section</h4>
<p>Paragraph content with technical details.</p>

<!-- References and links -->
<ul>
<li><b>Reference Name:</b> <a href="URL">Link Description</a></li>
</ul>
</article>

<hr>
```

### Content Guidelines

**Title Format:**
- Use descriptive, technical titles
- Keep titles concise but informative
- Use title case (capitalize major words)

**Date Format:**
- Use format: "Month DD, YYYY" (e.g., "June 22, 2025")
- Wrap in `<i>` tags for italic styling
- Place immediately after title

**Section Organization:**
- Use `<h4>` for main sections
- Add `id` attributes for sections that might be referenced
- Use bullet points (`<ul><li>`) for structured information
- Bold key terms with `<b>` tags

**Link Formatting:**
- Use descriptive link text, not just URLs
- Include external links to papers, videos, documentation
- Format as: `<a href="URL">Descriptive Text</a>`

**Technical Content:**
- Bold important terms and concepts
- Use bullet points for lists of features, techniques, or references
- Include relevant external links to papers, videos, GitHub repos
- Maintain technical accuracy and depth

### Example Blog Post Template

```html
<article>
<h3>Your Blog Post Title Here</h3>
<p><i>August 25, 2025</i></p>

<p>Brief introduction explaining what this post covers and why it's relevant.</p>

<h4>Main Topic Section</h4>
<ul>
<li><b>Key Concept:</b> Explanation with technical details</li>
<li><b>Implementation:</b> How it works in practice</li>
<li><b>Benefits:</b> Why this matters for the field</li>
</ul>

<h4 id="technical-details">Technical Implementation</h4>
<p>Detailed explanation of technical concepts, methodologies, or findings.</p>

<h4>References and Resources</h4>
<ul>
<li><b>Research Paper:</b> <a href="https://arxiv.org/paper">Paper Title on arXiv</a></li>
<li><b>Documentation:</b> <a href="https://docs.example.com">Official Documentation</a></li>
<li><b>Video:</b> <a href="https://youtube.com/watch">Conference Talk Title</a></li>
</ul>
</article>

<hr>
```

### Adding a New Blog Post

1. **Open blog.html** in your editor

2. **Find the blog posts section** (after `<h2>BLOG POSTS</h2>`)

3. **Add your new post** at the top (most recent first) using the template above

4. **Follow the content guidelines** for consistent formatting

5. **Add horizontal rule** (`<hr>`) between posts for visual separation

### Content Categories

**Suitable blog post topics:**
- Technical research and findings
- AI/ML model analysis and insights
- Hardware and system architecture discussions
- Conference notes and key takeaways
- Tool and framework comparisons
- Industry trend analysis
- Resource compilations and curated lists

### Styling (Automatic)

The engineering arts CSS automatically applies:
- ✅ Monospace typography for technical feel
- ✅ Consistent spacing and margins
- ✅ Clean link styling with hover effects
- ✅ Proper heading hierarchy
- ✅ Readable line spacing and typography
- ✅ Responsive layout for all devices

### Best Practices

**Content Quality:**
- Focus on technical depth and accuracy
- Include relevant external references
- Provide actionable insights or learnings
- Maintain professional, informative tone

**Formatting Consistency:**
- Use the same date format across all posts
- Maintain consistent section structure
- Apply bold formatting to key terms uniformly
- Include proper links with descriptive text

**Organization:**
- Place newest posts at the top
- Use clear, descriptive section headings
- Group related information in bullet points
- Separate posts with horizontal rules

### File Management

**Location:** All blog content goes in `/blog.html`
**Backup:** Consider keeping draft content in separate files before adding to blog.html
**Version Control:** Commit changes with descriptive commit messages

The blog maintains the engineering arts aesthetic while providing a clean, readable format for technical content and research insights.
