# ASMA Patterns

A pattern is a recurring workflow or interaction model composed of multiple
components. It is not a one-off screen composition.

Candidate patterns:
- Form
- Search
- FilterBar
- QueryBuilder
- DataTable
- BulkActions
- FileUpload
- DetailView
- MasterDetail
- Confirmation
- Authentication
- NotificationCenter
- EmptyState
- ErrorState
- LoadingState

Built patterns (see Figma page "Navigation", under the top-level "Patterns" section):
- Sidebar — persistent SaaS navigation, built from Menu-item. Variant Mode=Expanded/Collapsed (icon-only, 64px, reuses Show-label=false on its Menu-item instances).
- Topbar (SaaS) — global search/notifications/account bar, complements Sidebar. Uses a real Avatar instance (Type=Initials, Size=Medium).
- Site-nav (vitrine) — flat marketing site navigation with CTA, no user account context

Pattern specs should contain: Purpose, Use when, Do not use when, Components,
Structure, Interaction flow, States, Validation/errors, Accessibility,
Responsive behavior, Tokens and Related components/patterns.
