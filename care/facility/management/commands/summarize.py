from django.core.management.base import BaseCommand

from care.facility.summarisation.district.patient_summary import DistrictPatientSummary
from care.facility.summarisation.facility_capacity import FacilityCapacitySummary
from care.facility.summarisation.patient_summary import PatientSummary


class Command(BaseCommand):
    """
    Management command to Force Create Summary objects.
    """

    help = "Force Create Summary Objects"

    def handle(self, *args, **options):
        PatientSummary()
        print("Patients Summarised")
        FacilityCapacitySummary()
        print("Capacity Summarised")
        DistrictPatientSummary()
        print("District Wise Patient Summarised")
