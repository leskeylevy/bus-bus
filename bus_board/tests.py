from django.test import TestCase
from .models import BusOrganisation, Route, Bus

# Create your tests here.
class BusOrganisationTestClass(TestCase):
    '''
    Test case for the Bus Organisation class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Bus Organisation class
        '''
        # Create instance of Bus Organisation class
        self.new_bus_organisation = BusOrganisation(name='Kiki And Son ltd')

    def test_instance(self):
        '''
        Test case to check if self.new_bus_organisation in an instance of Bus Organisation class
        '''
        self.assertTrue( isinstance(self.new_bus_organisation, BusOrganisation) )

    def test_get_bus_organisations(self):
        '''
        Test to check if all bus organisations are gotten from the database
        '''
        self.new_bus_organisation.save()

        self.test_bus_organisation = BusOrganisation(name="Anothe Bus Ltd")

        self.test_bus_organisation.save()

        gotten_buses = BusOrganisation.get_bus_organisations()

        bus_organisations = BusOrganisation.objects.all()

        self.assertTrue( len(gotten_buses) == len(bus_organisations) )

    def test_get_single_bus_organisation(self):
        '''
        Test to check if the specified bus organisation is gotten from the database
        '''
        self.new_bus_organisation.save()

        self.test_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.test_bus_organisation.save()

        gotten_bus = BusOrganisation.get_single_bus_organisation(self.new_bus_organisation.id)

        # bus_organisations = BusOrganisation.objects.all()
        
        self.assertTrue( isinstance(gotten_bus, BusOrganisation))

class RouteTestClass(TestCase):
    '''
    Test case for the Route class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Route class
        '''
        # Create instance of Route class
        self.new_route = Route(departure_location='Nairobi', destination_location='Mombasa')

    def test_instance(self):
        '''
        Test case to check if self.new_route in an instance of Route class
        '''
        self.assertTrue( isinstance(self.new_route, Route) )

    def test_get_routes(self):
        '''
        Test to check if all routes are gotten from the database
        '''
        self.new_route.save()

        self.test_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.test_route.save()

        gotten_routes = Route.get_routes()

        routes = Route.objects.all()

        self.assertTrue( len(gotten_routes) == len(routes) )

    def test_get_single_route(self):
        '''
        Test to check if the specified route is gotten from the database
        '''
        self.new_route.save()

        self.test_route = Route(departure_location='Naivasha', destination_location='Nairobi')

        self.test_route.save()

        gotten_route= Route.get_single_route(self.new_route.id)

        # routes = Route.objects.all()
        
        self.assertTrue( isinstance(gotten_route, Route))

class BusTestClass(TestCase):
    '''
    Test case for the Bus class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Bus class
        '''
        # Create instance of Bus Organisation class
        self.test_bus_organisation = BusOrganisation(name='Kiki And Son ltd')

        self.test_bus_organisation.save()

        # Create instance of Route class
        self.test_route = Route(departure_location='Nairobi', destination_location='Mombasa')

        self.test_route.save()

        # Create instance of Bus class
        self.new_bus = Bus(bus_organisation=self.test_bus_organisation, number_plate='KBC 243J', route=self.test_route, capacity=34 )

    def test_instance(self):
        '''
        Test case to check if self.new_bus in an instance of Route class
        '''
        self.assertTrue( isinstance(self.new_bus, Bus) )

    def test_get_buses(self):
        '''
        Test to check if all buses are gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        gotten_buses = Bus.get_buses()

        buses = Bus.objects.all()

        self.assertTrue( len(gotten_buses) == len(buses) )

    def test_get_single_bus(self):
        '''
        Test to check if the specified bus is gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        gotten_bus = Bus.get_single_bus(self.new_bus.id)

        # buses = Bus.objects.all()
        
        self.assertTrue( isinstance(gotten_bus, Bus))

    def test_get_bus_organisation_buses(self):
        '''
        Test to check if all buses for a specific bus organisation are gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        self.test_bus2 = Bus(bus_organisation=self.another_bus_organisation, number_plate='KBY 312T', route=self.test_route, capacity=38 )

        self.test_bus2.save()

        gotten_buses = Bus.get_bus_organisation_buses(self.another_bus_organisation.id)

        buses = Bus.objects.all()

        self.assertTrue( len(gotten_buses) != len(buses) )

    def test_get_route_buses(self):
        '''
        Test to check if all buses for a specific bus route are gotten from the database
        '''
        self.new_bus.save()

        self.another_bus_organisation = BusOrganisation(name="Another Bus Ltd")

        self.another_bus_organisation.save()

        self.another_route = Route(departure_location='Nakuru', destination_location='Nairobi')

        self.another_route.save()

        self.test_bus = Bus(bus_organisation=self.another_bus_organisation, number_plate='KCJ 523T', route=self.another_route, capacity=44 )

        self.test_bus.save()

        self.test_bus2 = Bus(bus_organisation=self.test_bus_organisation, number_plate='KBY 312T', route=self.another_route, capacity=38 )

        self.test_bus2.save()

        gotten_buses = Bus.get_route_buses(self.another_route.id)

        buses = Bus.objects.all()

        self.assertTrue( len(gotten_buses) != len(buses) )





