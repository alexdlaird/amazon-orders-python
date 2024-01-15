import unittest
from datetime import date

__author__ = "Alex Laird"
__copyright__ = "Copyright 2024, Alex Laird"
__version__ = "0.0.5"


class TestCase(unittest.TestCase):
    def assert_order_112_0399923_3070642(self, order, full_details):
        self.assertEqual("34.01", order.grand_total)
        self.assertEqual("112-0399923-3070642", order.order_number)
        self.assertIsNotNone(order.order_details_link)
        self.assertEqual(date(2018, 12, 21), order.order_placed_date)
        self.assertEqual("Alex Laird", order.recipient.name)
        self.assertIsNotNone(order.recipient.address)
        self.assertEqual(1, len(order.shipments))
        self.assertEqual(str(order.items), str(order.shipments[0].items))
        self.assertEqual(order, order.shipments[0].order)
        self.assertIsNone(order.shipments[0].delivery_status)
        self.assertIsNone(order.shipments[0].tracking_link)
        self.assertEqual(1, len(order.items))
        self.assertEqual(
            "Taste Of The Wild Rocky Mountain Grain-Free Dry Cat Food With Roasted Venison & Smoked Salmon 15Lb",
            order.items[0].title)
        self.assertIsNotNone(order.items[0].link)
        self.assertEqual(date(2019, 2, 2),
                         order.items[0].return_eligible_date)

        self.assertEqual(order.full_details, full_details)

        if full_details:
            self.assertEqual("American Express", order.payment_method)
            self.assertEqual(4, len(order.payment_method_last_4))
            self.assertEqual("30.99", order.subtotal)
            self.assertEqual("0.00", order.shipping_total)
            self.assertIsNone(order.subscription_discount)
            self.assertEqual("30.99", order.total_before_tax)
            self.assertEqual("3.02", order.estimated_tax)
            self.assertEqual(date(2018, 12, 28), order.order_shipped_date)
            self.assertEqual("New", order.items[0].condition)
            self.assertEqual("30.99", order.items[0].price)
            self.assertEqual("Amazon.com Services, Inc",
                             order.items[0].seller.name)
            self.assertIsNone(order.items[0].seller.link)

    def assert_order_114_9460922_7737063(self, order, full_details):
        self.assertEqual("35.90", order.grand_total)
        self.assertEqual("114-9460922-7737063", order.order_number)
        self.assertIsNotNone(order.order_details_link)
        self.assertEqual(date(2020, 10, 27), order.order_placed_date)
        self.assertEqual("Alex Laird", order.recipient.name)
        self.assertIsNotNone(order.recipient.address)
        self.assertEqual(1, len(order.shipments))
        self.assertEqual(str(order.items),
                         str(order.shipments[0].items))
        self.assertEqual(str(order),
                         str(order.shipments[0].order))
        self.assertIsNone(order.shipments[0].tracking_link)
        self.assertIsNone(order.shipments[0].delivery_status)
        self.assertEqual(1, len(order.items))
        self.assertEqual("Bounty Quick-Size Paper Towels, White, 16 Family Rolls = 40 Regular Rolls",
                         order.items[0].title)
        self.assertIsNotNone(order.items[0].link)
        self.assertIsNone(order.items[0].return_eligible_date)

        self.assertEqual(order.full_details, full_details)

        if full_details:
            self.assertEqual("American Express", order.payment_method)
            self.assertEqual(4, len(order.payment_method_last_4))
            self.assertEqual("38.84", order.subtotal)
            self.assertEqual("0.00", order.shipping_total)
            self.assertEqual("-5.83", order.subscription_discount)
            self.assertEqual("33.01", order.total_before_tax)
            self.assertEqual("2.89", order.estimated_tax)
            self.assertEqual(date(2020, 10, 28), order.order_shipped_date)
            self.assertEqual("New", order.items[0].condition)
            self.assertEqual("38.84", order.items[0].price)
            self.assertEqual("Amazon.com Services, Inc",
                             order.items[0].seller.name)
            self.assertIsNone(order.items[0].seller.link)

    def assert_order_112_2961628_4757846_return(self, order, full_details):
        self.assertEqual("76.11", order.grand_total)
        self.assertEqual("112-2961628-4757846", order.order_number)
        self.assertIsNotNone(order.order_details_link)
        self.assertEqual(date(2020, 10, 18), order.order_placed_date)
        self.assertEqual("Alex Laird", order.recipient.name)
        self.assertIsNotNone(order.recipient.address)
        self.assertEqual(1, len(order.shipments))
        self.assertEqual(str(order.items),
                         str(order.shipments[0].items))
        self.assertEqual(str(order),
                         str(order.shipments[0].order))
        self.assertIsNone(order.shipments[0].tracking_link)
        self.assertTrue("Return complete", order.shipments[0].delivery_status)
        self.assertEqual(1, len(order.items))
        self.assertEqual("Nintendo Switch Pro Controller",
                         order.items[0].title)
        self.assertIsNotNone(order.items[0].link)
        self.assertIsNone(order.items[0].return_eligible_date)

        self.assertEqual(order.full_details, full_details)

        if full_details:
            self.assertEqual("American Express", order.payment_method)
            self.assertEqual(4, len(order.payment_method_last_4))
            self.assertEqual("69.99", order.subtotal)
            self.assertEqual("0.00", order.shipping_total)
            self.assertIsNone(order.subscription_discount)
            self.assertEqual("69.99", order.total_before_tax)
            self.assertEqual("6.12", order.estimated_tax)
            self.assertEqual("76.11", order.refund_total)
            self.assertEqual(date(2020, 10, 19), order.order_shipped_date)
            self.assertTrue(date(2020, 11, 2), order.refund_completed_date)
            self.assertEqual("New", order.items[0].condition)
            self.assertEqual("69.99", order.items[0].price)
            self.assertEqual("Amazon.com Services, Inc",
                             order.items[0].seller.name)
            self.assertIsNone(order.items[0].seller.link)

    def assert_order_112_9685975_5907428_multiple_items_shipments_sellers(self, order, full_details, history_page):
        self.assertEqual("46.61", order.grand_total)
        self.assertEqual("112-9685975-5907428", order.order_number)
        if history_page:
            self.assertIsNotNone(order.order_details_link)
        else:
            self.assertIsNone(order.order_details_link)
        self.assertEqual(date(2023, 12, 7), order.order_placed_date)
        self.assertEqual("Alex Laird", order.recipient.name)
        self.assertIsNotNone(order.recipient.address)
        self.assertEqual(2, len(order.shipments))
        found_cadeya = False
        found_amazon = False
        for shipment in order.shipments:
            self.assertEqual(1, len(shipment.items))
            self.assertEqual(str(order),
                             str(shipment.order))
            order_item = filter(lambda i: i.title == shipment.items[0].title, order.items).next()
            self.assertEqual(str(order_item),
                             str(shipment.items[0]))
            if "Cadeya" in shipment.items[0].title:
                found_cadeya = True
                self.assertIsNotNone(shipment.tracking_link)
                self.assertEqual("Delivered Dec 9, 2023", shipment.delivery_status)
            else:
                found_amazon = True
                self.assertIsNotNone(shipment.tracking_link)
                self.assertEqual("Delivered Dec 8, 2023", shipment.delivery_status)
        self.assertTrue(found_cadeya)
        self.assertTrue(found_amazon)
        self.assertEqual(str(order.items),
                         str(order.shipments[0].items + order.shipments[1].items))
        self.assertEqual(2, len(order.items))
        found_cadeya = False
        found_amazon = False
        for order_item in order.items:
            if "Cadeya" in order_item.title:
                found_cadeya = True
                self.assertEqual(
                    "Cadeya Egg Cleaning Brush Silicone, Egg Scrubber for Fresh Eggs, Reusable Cleaning Tools for Egg Washer (Pink)",
                    order_item.title)
                self.assertIsNotNone(order_item.link)
                self.assertEqual(date(2024, 1, 31), order_item.return_eligible_date)
            else:
                found_amazon = True
                self.assertEqual(
                    "Swiffer WetJet Hardwood and Floor Spray Mop Cleaner Starter Kit, Includes: 1 Power Mop, 10 Pads, Cleaning Solution, Batteries",
                    order_item.title)
                self.assertIsNotNone(order_item.link)
                self.assertEqual(date(2024, 1, 31), order_item.return_eligible_date)
        self.assertTrue(found_cadeya)
        self.assertTrue(found_amazon)

        self.assertEqual(order.full_details, full_details)

        if full_details:
            self.assertEqual("American Express", order.payment_method)
            self.assertEqual(4, len(order.payment_method_last_4))
            self.assertEqual("43.23", order.subtotal)
            self.assertEqual("0.00", order.shipping_total)
            self.assertIsNone(order.subscription_discount)
            self.assertEqual("43.23", order.total_before_tax)
            self.assertEqual("3.38", order.estimated_tax)
            self.assertEqual(date(2023, 12, 7), order.order_shipped_date)
            self.assertEqual("New", order.items[0].condition)
            self.assertEqual("14.99", order.items[0].price)
            self.assertEqual("New", order.items[1].condition)
            self.assertEqual("28.24", order.items[1].price)
            found_cadeya = False
            found_amazon = False
            for order_item in order.items:
                seller = order_item.seller
                if "Cadeya" in seller.name:
                    found_cadeya = True
                    self.assertEqual("Cadeya", seller.name)
                    self.assertIsNotNone(seller.link)
                else:
                    found_amazon = True
                    self.assertEqual("Amazon.com Services, Inc",
                                     seller.name)
                    self.assertIsNone(seller.link)
            self.assertTrue(found_cadeya)
            self.assertTrue(found_amazon)

    def assert_order_113_1625648_3437067_multiple_items(self, order, full_details):
        self.assertEqual("113-1625648-3437067", order.order_number)
        self.assertEqual(1, len(order.shipments))
        self.assertEqual(2, len(order.items))
        self.assertEqual(str(order.items),
                         str(order.shipments[0].items))
        self.assertEqual(str(order),
                         str(order.shipments[0].order))
        found_aa = False
        found_aaa = False
        for item in order.items:
            if "AA" in item.title:
                found_aa = True
                self.assertEqual(
                    "AmazonBasics 48 Pack AA High-Performance Alkaline Batteries, 10-Year Shelf Life, Easy to Open Value Pack",
                    item.title)
                self.assertIsNotNone(item.link)
                # TODO: this actually is shown on the page, it's just collapsed, should fix
                self.assertIsNone(item.return_eligible_date)
            else:
                found_aaa = True
                self.assertEqual(
                    "AmazonBasics 36 Pack AAA High-Performance Alkaline Batteries, 10-Year Shelf Life, Easy to Open Value Pack",
                    item.title)
                self.assertIsNotNone(item.link)
                # TODO: this actually is shown on the page, it's just collapsed, should fix
                self.assertIsNone(item.return_eligible_date)
        self.assertTrue(found_aa)
        self.assertTrue(found_aaa)

        self.assertEqual(order.full_details, full_details)

        if full_details:
            self.assertEqual("American Express", order.payment_method)
            self.assertEqual(4, len(order.payment_method_last_4))
            self.assertEqual("28.80", order.subtotal)
            self.assertEqual("0.00", order.shipping_total)
            self.assertIsNone(order.subscription_discount)
            self.assertEqual("28.80", order.total_before_tax)
            self.assertEqual("2.32", order.estimated_tax)
            self.assertEqual(date(2020, 10, 27), order.order_shipped_date)
            found_aa = False
            found_aaa = False
            for item in order.items:
                if "AA" in item.title:
                    found_aa = True
                    self.assertEqual("New", item.condition)
                    self.assertEqual("15.49", item.price)
                    self.assertEqual("Amazon.com Services, Inc",
                                     item.seller.name)
                    self.assertIsNone(item.seller.link)
                else:
                    found_aaa = True
                    self.assertEqual("New", item.condition)
                    self.assertEqual("10.99", item.price)
                    self.assertEqual("Amazon.com Services, Inc",
                                     item.seller.name)
                    self.assertIsNone(item.seller.link)
            self.assertTrue(found_aa)
            self.assertTrue(found_aaa)