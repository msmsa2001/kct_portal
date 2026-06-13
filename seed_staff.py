"""
Seed dummy StaffMember rows for testing the "Our Team" section.

Usage (from the project root, with the same env Django normally runs in):
    python seed_staff.py            # add dummy staff
    python seed_staff.py --clear    # remove the dummy staff added by this script

Photos referenced below must exist in MEDIA_ROOT/staff/ (staff_1.jpg ... staff_4.jpg).
"""

import os
import sys

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kct_portal.settings")
django.setup()

from kct.models import StaffMember  # noqa: E402  (import after django.setup)


DUMMY_STAFF = [
    {
        "name": "Dr. Sara Khan",
        "designation": "Program Director",
        "photo": "staff/staff_1.jpg",
        "order": 1,
    },
    {
        "name": "Mr. Ahmed Sheikh",
        "designation": "Operations Manager",
        "photo": "staff/staff_2.jpg",
        "order": 2,
    },
    {
        "name": "Ms. Fatima Ali",
        "designation": "Community Outreach Lead",
        "photo": "staff/staff_3.jpg",
        "order": 3,
    },
    {
        "name": "Mr. Rahul Verma",
        "designation": "Finance Officer",
        "photo": "staff/staff_4.jpg",
        "order": 4,
    },
    {
        "name": "Ms. Ayesha Siddiqui",
        "designation": "Project Coordinator",
        "photo": "staff/staff_5.jpg",
        "order": 5,
    },
    {
        "name": "Mr. Vikram Patel",
        "designation": "Volunteer Manager",
        "photo": "staff/staff_6.jpg",
        "order": 6,
    },
    {
        "name": "Dr. Imran Qureshi",
        "designation": "Medical Advisor",
        "photo": "staff/staff_7.jpg",
        "order": 7,
    },
    {
        "name": "Ms. Neha Sharma",
        "designation": "HR Executive",
        "photo": "staff/staff_8.jpg",
        "order": 8,
    },
    {
        "name": "Mr. Kabir Ansari",
        "designation": "Field Officer",
        "photo": "staff/staff_9.jpg",
        "order": 9,
    },
    {
        "name": "Ms. Priya Nair",
        "designation": "Communications Lead",
        "photo": "staff/staff_10.jpg",
        "order": 10,
    },
]


def add():
    created = 0
    for data in DUMMY_STAFF:
        obj, was_created = StaffMember.objects.get_or_create(
            name=data["name"], defaults=data
        )
        if was_created:
            created += 1
            print(f"  + created: {obj.name}")
        else:
            print(f"  = already exists, skipped: {obj.name}")
    print(f"Done. {created} new staff member(s) added.")


def clear():
    names = [d["name"] for d in DUMMY_STAFF]
    deleted, _ = StaffMember.objects.filter(name__in=names).delete()
    print(f"Done. Removed {deleted} dummy staff record(s).")


if __name__ == "__main__":
    if "--clear" in sys.argv:
        clear()
    else:
        add()
