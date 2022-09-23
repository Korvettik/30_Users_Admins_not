import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from category.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
	model = Category

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)

		categories = self.object_list

		result = []
		for category in categories:
			result.append({
				'id': category.id,
				'name': category.name
			})
		return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
	model = Category

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)
		category = self.get_object()

		return JsonResponse({
			'id': category.id,
			'name': category.name
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
	model = Category
	fields = ['name']

	def post(self, request, *args, **kwargs):
		super().post(request, *args, **kwargs)

		data = json.loads(request.body)

		category = Category.objects.create(
			name=data.get('name')
		)

		return JsonResponse({
			'id': category.id,
			'name': category.name
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
	model = Category
	fields = ['name']

	def patch(self, request, *args, **kwargs):
		super().post(request, *args, **kwargs)

		data = json.loads(request.body)
		category = self.object

		category.name = data.get('name', category.name)

		category.save()

		return JsonResponse({
			'id': category.id,
			'name': category.name
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
	model = Category
	success_url = '/'

	def delete(self, request, *args, **kwargs):
		super().delete(request, *args, **kwargs)

		return JsonResponse({'status': 'ok'})
