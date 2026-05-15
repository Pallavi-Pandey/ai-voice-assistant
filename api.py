import sqlite3
import os

from livekit.agents.llm import function_tool

DB_PATH = os.path.join(os.path.dirname(__file__), "vehicles.db")


def _init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            vin        TEXT PRIMARY KEY,
            make       TEXT NOT NULL,
            model      TEXT NOT NULL,
            year       INTEGER NOT NULL,
            owner_name TEXT NOT NULL,
            phone      TEXT,
            email      TEXT
        )
    """)
    conn.commit()
    conn.close()


_init_db()


@function_tool
async def lookup_vin(vin: str) -> str:
    """Look up a vehicle record by its VIN number.

    Args:
        vin: The 17-character vehicle identification number to search for
    """
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT vin, make, model, year, owner_name, phone, email FROM vehicles WHERE vin = ?",
        (vin.strip().upper(),),
    ).fetchone()
    conn.close()

    if row:
        vin_val, make, model, year, owner, phone, email = row
        return (
            f"Vehicle found — VIN: {vin_val}, {year} {make} {model}, "
            f"Owner: {owner}, Phone: {phone or 'N/A'}, Email: {email or 'N/A'}"
        )
    return f"No vehicle found with VIN {vin.strip().upper()}."


@function_tool
async def create_vehicle(
    vin: str,
    make: str,
    model: str,
    year: int,
    owner_name: str,
    phone: str,
    email: str,
) -> str:
    """Create a new vehicle and customer profile in the database.

    Args:
        vin: The 17-character vehicle identification number
        make: Vehicle make or brand, e.g. Toyota
        model: Vehicle model name, e.g. Camry
        year: Four-digit model year, e.g. 2021
        owner_name: Full name of the vehicle owner
        phone: Owner phone number, use empty string if unknown
        email: Owner email address, use empty string if unknown
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "INSERT INTO vehicles (vin, make, model, year, owner_name, phone, email) VALUES (?,?,?,?,?,?,?)",
            (vin.strip().upper(), make, model, year, owner_name, phone, email),
        )
        conn.commit()
        return f"Profile created for {owner_name} with VIN {vin.strip().upper()}."
    except sqlite3.IntegrityError:
        return f"A vehicle with VIN {vin.strip().upper()} already exists."
    finally:
        conn.close()


@function_tool
async def update_contact(vin: str, phone: str, email: str) -> str:
    """Update phone or email for an existing vehicle owner.

    Args:
        vin: VIN of the vehicle whose owner contact should be updated
        phone: New phone number, use empty string to leave unchanged
        email: New email address, use empty string to leave unchanged
    """
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT vin FROM vehicles WHERE vin = ?", (vin.strip().upper(),)
    ).fetchone()
    if not row:
        conn.close()
        return f"No vehicle found with VIN {vin.strip().upper()}."

    if phone:
        conn.execute(
            "UPDATE vehicles SET phone = ? WHERE vin = ?", (phone, vin.strip().upper())
        )
    if email:
        conn.execute(
            "UPDATE vehicles SET email = ? WHERE vin = ?", (email, vin.strip().upper())
        )
    conn.commit()
    conn.close()
    return f"Contact updated for VIN {vin.strip().upper()}."


TOOLS = [lookup_vin, create_vehicle, update_contact]
