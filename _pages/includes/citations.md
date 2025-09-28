{% assign total_citations = site.data.google_scholar_stats.citedby %}
{% assign scholar_url = site.author.googlescholar %}
{% assign updated_text = site.data.google_scholar_stats.updated | default: "" %}

<div class="scholar-metrics">
  <div class="scholar-metrics__card">
    <div class="scholar-metrics__label">Google Scholar</div>
    <div class="scholar-metrics__count" id="total_cit" aria-live="polite">{{ total_citations | default: "--" }}</div>
    <div class="scholar-metrics__description">Total citations across all publications.</div>
    <div class="scholar-metrics__actions">
      <a class="btn btn--primary" href="{{ scholar_url }}" target="_blank" rel="noopener">View profile</a>
    </div>
    <div class="scholar-metrics__meta{% if updated_text == "" %} is-hidden{% endif %}" id="scholar_updated">
      Last updated: <span id="scholar_updated_value">{{ updated_text }}</span>
    </div>
  </div>
</div>
