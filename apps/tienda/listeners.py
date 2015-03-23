import logging
from getpaid import signals

logger = logging.getLogger('getpaid_test_project')

def new_payment_query_listener(sender, order=None, payment=None, **kwargs):
    payment.amount = order.total
    payment.currency = 'CLP'

getpaid.signals.new_payment_query.connect(new_payment_query_listener)

def payment_status_changed_listener(sender, instance, old_status, new_status, **kwargs):
    """
    Here we will actually do something, when payment is accepted.
    E.g. lets change an order status.
    """
    if old_status != 'paid' and new_status == 'paid':
        # Ensures that we process order only one
        instance.order.paid = True
        instance.order.save()

signals.payment_status_changed.connect(payment_status_changed_listener)


