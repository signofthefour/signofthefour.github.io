{% assign total_citations = site.data.google_scholar_stats.citedby %}
{% assign scholar_url = site.author.googlescholar %}

<div class="scholar-metrics">
  <div class="scholar-metrics__card">
    <div class="scholar-metrics__label">Google Scholar</div>
    <div class="scholar-metrics__count" id="total_cit">{{ total_citations | default: "--" }}</div>
    <div class="scholar-metrics__description">Total citations across all publications.</div>
    <div class="scholar-metrics__actions">
      <a class="btn btn--primary" href="{{ scholar_url }}" target="_blank" rel="noopener">View profile</a>
    </div>
    {% if site.data.google_scholar_stats.updated %}
    <div class="scholar-metrics__meta">Last updated: {{ site.data.google_scholar_stats.updated }}</div>
    {% endif %}
  </div>
</div>
