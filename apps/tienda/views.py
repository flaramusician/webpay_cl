# Create your views here.
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from getpaid.forms import PaymentMethodForm
from .forms import OrderForm
from .models import Order

class HomeView(CreateView):
	model=Order
	template_name='index.html'
	form_class=OrderForm


	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['orders'] = Order.objects.all()
		return context



class OrderView(DetailView):
	model=Order


	def get_context_data(self, **kwargs):
		context = super(OrderView, self).get_context_data(**kwargs)
		context['payment_form'] = PaymentMethodForm(self.object.currency, initial={'order': self.object})
		return context
