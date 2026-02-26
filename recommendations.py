def get_ai_recommendations(row):
    """
    Logic to provide optimization suggestions based on the leak score.
    """
    if row['Leak_Score'] > 15:
        return "CRITICAL: Heavy appliance left ON in empty room. Remote shutdown recommended."
    elif row['Leak_Score'] > 5:
        return "WARNING: Moderate energy waste detected. Check lights and fans."
    elif row['Leak_Score'] > 0:
        return "MINOR: Slight energy deviation. Monitor for patterns."
    else:
        return "OPTIMIZED: Energy usage aligns with occupancy."