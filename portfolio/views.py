
from django.views import View
from django.shortcuts import render


class PortfolioView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='portfolio/index.html'
        )
