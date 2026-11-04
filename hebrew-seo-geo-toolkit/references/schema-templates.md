# JSON-LD Schema Templates

Ready-to-use JSON-LD structured data templates for SEO and GEO optimization.

**Google rich-result status (checked 2026-11-03):** FAQ rich results stopped appearing on 7 May 2026, HowTo rich results were removed in September 2023, and Speakable works only for English-language news publishers in the US. Those templates remain valid schema.org for other consumers, but promise no Google result from them. Google also says structured data is not required for generative AI search.

---

## 1. FAQPage Schema

**Best for:** consumers other than Google. No Google rich result since 7 May 2026.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is [Your Product/Service]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Comprehensive answer with statistics. According to <source>, <N>% of users report <benefit>.]"
      }
    },
    {
      "@type": "Question",
      "name": "How does [Product/Service] work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Step-by-step explanation. First, you... Then... Finally...]"
      }
    },
    {
      "@type": "Question",
      "name": "What are the benefits of [Product/Service]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[List key benefits with data. Users save an average of X hours per week.]"
      }
    },
    {
      "@type": "Question",
      "name": "How much does [Product/Service] cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Pricing information. Plans start at $X/month with a free tier available.]"
      }
    },
    {
      "@type": "Question",
      "name": "How do I get started with [Product/Service]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Plain-language answer describing how to get started, for example the steps to sign up or contact you]"
      }
    }
  ]
}
```

---

## 2. WebPage Schema

**Best for:** Standard content pages, landing pages.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Page Title]",
  "description": "[Page description]",
  "url": "https://example.com/page",
  "datePublished": "2024-01-15",
  "dateModified": "2024-12-20",
  "inLanguage": "he",
  "isPartOf": {
    "@type": "WebSite",
    "name": "[Site Name]",
    "url": "https://example.com"
  },
  "author": {
    "@type": "Person",
    "name": "[Author Name]",
    "url": "https://example.com/about"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[Organization Name]",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
```

---

## 3. Article Schema

**Best for:** Blog posts, news articles, tutorials.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Article Title, concise]",
  "description": "[Article summary]",
  "image": [
    "https://example.com/image-1x1.jpg",
    "https://example.com/image-4x3.jpg",
    "https://example.com/image-16x9.jpg"
  ],
  "datePublished": "2024-01-15T08:00:00+00:00",
  "dateModified": "2024-12-20T10:30:00+00:00",
  "author": {
    "@type": "Person",
    "name": "[Author Name]",
    "url": "https://example.com/author/name",
    "jobTitle": "[Job Title]",
    "worksFor": {
      "@type": "Organization",
      "name": "[Company]"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher Name]",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png",
      "width": 600,
      "height": 60
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article-url"
  },
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "articleSection": "[Category]",
  "wordCount": 2500
}
```

---

## 4. SoftwareApplication Schema

**Best for:** Tools, apps, software products.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[App Name]",
  "description": "[App description]",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "url": "https://example.com",
  "downloadUrl": "https://example.com/download",
  "softwareVersion": "1.0.0",
  "releaseNotes": "https://example.com/changelog",
  "screenshot": "https://example.com/screenshot.png",
  "featureList": [
    "Feature 1 description",
    "Feature 2 description",
    "Feature 3 description"
  ],
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "ILS",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "150",
    "bestRating": "5",
    "worstRating": "1"
  },
  "author": {
    "@type": "Organization",
    "name": "[Company Name]",
    "url": "https://example.com"
  }
}
```

---

## 5. Organization Schema

**Best for:** About pages, company pages.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Organization Name]",
  "alternateName": "[Alternate Name]",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "[Organization description]",
  "foundingDate": "2024",
  "founders": [
    {
      "@type": "Person",
      "name": "[Founder Name]"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "[City]",
    "addressCountry": "IL"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "support@example.com"
  },
  "sameAs": [
    "{your-x-profile-url}",
    "{your-github-url}",
    "{your-linkedin-company-url}"
  ]
}
```

---

## 6. Product Schema

**Best for:** E-commerce product pages.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "description": "[Product description]",
  "image": [
    "https://example.com/product-image-1.jpg",
    "https://example.com/product-image-2.jpg"
  ],
  "sku": "[SKU]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product",
    "priceCurrency": "ILS",
    "price": "99.99",
    "priceValidUntil": "[YYYY-MM-DD, a future date]",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "[Seller Name]"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "89"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "[Reviewer Name]"
      },
      "reviewBody": "[Review text]"
    }
  ]
}
```

---

## 7. HowTo Schema

**Best for:** consumers other than Google. No Google rich result since September 2023.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [Do Something]",
  "description": "[Brief description of what this guide covers]",
  "image": "https://example.com/how-to-image.jpg",
  "totalTime": "PT15M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "ILS",
    "value": "0"
  },
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "[Required item 1]"
    }
  ],
  "tool": [
    {
      "@type": "HowToTool",
      "name": "[Required tool 1]"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Step 1: [Step Name]",
      "text": "[Detailed step instructions]",
      "image": "https://example.com/step-1.jpg",
      "url": "https://example.com/guide#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Step 2: [Step Name]",
      "text": "[Detailed step instructions]",
      "image": "https://example.com/step-2.jpg",
      "url": "https://example.com/guide#step2"
    },
    {
      "@type": "HowToStep",
      "name": "Step 3: [Step Name]",
      "text": "[Detailed step instructions]",
      "image": "https://example.com/step-3.jpg",
      "url": "https://example.com/guide#step3"
    }
  ]
}
```

---

## 8. BreadcrumbList Schema

**Best for:** All pages with navigation hierarchy.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Category]",
      "item": "https://example.com/category"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Current Page]",
      "item": "https://example.com/category/page"
    }
  ]
}
```

---

## 9. LocalBusiness Schema (Israeli business)

**Best for:** Local business pages. Model the hours the owner actually keeps: many businesses open on Shabbat. To mark a day closed, Google says to set both `opens` and `closes` to "00:00". Keep `dayOfWeek` values in English.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "description": "[Business description in Hebrew]",
  "image": "https://example.co.il/business-image.jpg",
  "url": "https://example.co.il",
  "telephone": "+972-3-555-0000",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street and number]",
    "addressLocality": "[City]",
    "postalCode": "[7-digit postal code]",
    "addressCountry": "IL"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
      "opens": "09:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Friday",
      "opens": "09:00",
      "closes": "13:00"
    }
  ],
  "specialOpeningHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "validFrom": "2027-04-21",
      "validThrough": "2027-04-21",
      "opens": "09:00",
      "closes": "12:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "validFrom": "2027-04-22",
      "validThrough": "2027-04-22",
      "opens": "00:00",
      "closes": "00:00"
    }
  ]
}
```

The two special entries are Erev Pesach (short day) and the first day of Pesach 2027 (closed). Set the same special hours in Google Business Profile.

---

## 10. SpeakableSpecification (English-language US news only)

**Best for:** English-language news publishers in the US (Google Assistant). Not useful for a Hebrew business page; no AI engine documents reading it.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Page Title]",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      "h1",
      ".summary",
      ".key-takeaways",
      ".faq-answer"
    ]
  }
}
```

---

## Combined Schema Example

For an Israeli business home page, link the entities with `@id` in one `@graph`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.co.il/#org",
      "name": "[Business Name]",
      "url": "https://example.co.il",
      "logo": "https://example.co.il/logo.png",
      "sameAs": ["[Google Business Profile URL]", "[Facebook page URL]"]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.co.il/#website",
      "url": "https://example.co.il",
      "name": "[Site Name]",
      "inLanguage": "he",
      "publisher": {"@id": "https://example.co.il/#org"}
    },
    {
      "@type": "WebPage",
      "@id": "https://example.co.il/#webpage",
      "url": "https://example.co.il",
      "name": "[Page Title]",
      "inLanguage": "he",
      "isPartOf": {"@id": "https://example.co.il/#website"},
      "about": {"@id": "https://example.co.il/#org"}
    }
  ]
}
```

---

## Validation Tools

1. **Google Rich Results Test**
   ```
   https://search.google.com/test/rich-results?url={your-url}
   ```

2. **Schema.org Validator**
   ```
   https://validator.schema.org/?url={your-url}
   ```

3. **Google Search Console**
   - Check "Enhancements" for schema issues
   - Monitor rich result performance
