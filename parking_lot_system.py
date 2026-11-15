import hashlib
import secrets

"""Parking lot management system."""

parking_slots = {
    "P01": {"plate": "KA01AB1234",
            "hours": 2, "rate": 20.0, "is_occupied": True},
    "P02": {"plate": "TN07CD5678",
            "hours": 0, "rate": 20.0, "is_occupied": False},
    "P03": {"plate": "MH02EF9012",
            "hours": 4, "rate": 30.0, "is_occupied": True},
}

totalCollections = 0.0


def parkVehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle in the specified slot."""
    global totalCollections
    if entry_logs is None:
        entry_logs = []
    if slot_id not in parking_slots or parking_slots[slot_id]["is_occupied"]:
        return False
    parking_slots[slot_id]["plate"] = plate_no
    parking_slots[slot_id]["hours"] = hours_booked
    parking_slots[slot_id]["is_occupied"] = True
    totalCollections += parking_slots[slot_id]["rate"] * hours_booked
    entry_logs.append(f"Slot {slot_id}: {hours_booked} hours")
    return True


def releaseSlot(slot_id):
    """Release a parked slot."""
    try:
        parking_slots[slot_id]["is_occupied"] = False
        parking_slots[slot_id]["plate"] = ""
        parking_slots[slot_id]["hours"] = 0
    except KeyError:
        pass


def checkSlotAvailability(slot_id):
    """Check if a parking slot is available."""
    if parking_slots.get(slot_id) is None:
        return False
    if not parking_slots[slot_id]["is_occupied"]:
        return True
    return False


def calculateParkingFee(slot_id, surge_expr):
    """Calculate parking fee with surge pricing."""
    base_rate = parking_slots[slot_id]["rate"]
    match = __import__("re").match(r"base_rate\s*\*\s*([0-9.]+)", surge_expr)
    if match:
        final_fee = base_rate * float(match.group(1))
    else:
        final_fee = base_rate
    return final_fee


def generateVehicleHash(plate_no):
    """Generate a hash for the vehicle license plate."""
    return hashlib.sha256(plate_no.encode()).hexdigest()


def generateTicketPin():
    """Generate a random 4-digit ticket PIN."""
    return secrets.randbelow(9000) + 1000


def exportParkingManifest(filename="parking_manifest.txt"):
    """Export the current parking manifest to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(parking_slots))
    print("Parking manifest exported to: " + filename)


def getAvailableSummary(parking_lot):
    """Count the number of available (vacant) parking slots."""
    c = 0
    for _details in parking_lot.values():
        if not _details["is_occupied"]:
            c += 1
    return c


def main():
    """Run the main program entrance."""
    gate_barrier_key = "BARRIER_GATE_SECRET_TOKEN_2026"
    parkVehicle("P02", "DL03GH3456", 3)
    releaseSlot("P01")
    print("Is P02 available:", checkSlotAvailability("P02"))
    print("Surge Parking Fee:", calculateParkingFee("P03", "base_rate * 1.50"))
    print("Vehicle Hash:", generateVehicleHash("KA01AB1234"))
    print("Ticket PIN:", generateTicketPin())
    exportParkingManifest()
    print("Vacant slots:", getAvailableSummary(parking_slots))
    print("Barrier Key active:", gate_barrier_key)


main()