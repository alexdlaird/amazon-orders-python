import os

import responses

from amazonorders.exception import AmazonOrdersError
from amazonorders.orders import AmazonOrders

from amazonorders.session import AmazonSession, BASE_URL

from tests.testcase import UnitTestCase

__author__ = "Alex Laird"
__copyright__ = "Copyright 2024, Alex Laird"
__version__ = "0.0.3"


class TestOrderHistory(UnitTestCase):
    def setUp(self):
        self.amazon_session = AmazonSession("some-username", "some-password")

        self.amazon_orders = AmazonOrders(self.amazon_session)

    def test_get_orders_unauthenticated(self):
        # WHEN
        with self.assertRaises(AmazonOrdersError):
            self.amazon_orders.get_order_history()

    @responses.activate
    def test_get_orders(self):
        # GIVEN
        with open(os.path.join("resources", "orders.html"), "r") as f:
            responses.add(
                responses.GET,
                "{}/your-orders/orders?timeFilter=year-{}".format(BASE_URL, 2023),
                body=f.read(),
                status=200,
            )

        # THEN
        # TODO: write the rest of the test
