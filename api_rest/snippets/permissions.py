from rest_framework import permissions

class IsAuthenticatedOrCreated(permissions.IsAuthenticated):
	def has_permission(self, request, views):
		if request.method == 'POST':
			return True

		return super(IsAuthenticatedOrCreated, self).has_permission(request, views)
