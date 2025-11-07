def validasi_email(email):
    return "@" in email and "." in email and len(email) > 5

def validasi_umur(umur_str):
    try:
        umur = int(umur_str)
        return umur if 1 <= umur <= 150 else None
    except (ValueError, TypeError):
        return None
