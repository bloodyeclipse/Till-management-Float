
# Function to calculate change in denominations
def calculate_change(amount_paid, transaction_total):
    change = amount_paid - transaction_total
    denominations = [50, 20, 10, 5, 2, 1]
    change_breakdown = []
    
    for denomination in denominations:
        count = change // denomination
        if count > 0:
            change_breakdown.append(f"{denomination}*{count}")
            change -= count * denomination
    
    return change_breakdown

# Open the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Initialize till float
till_float = {'R50': 5, 'R20': 5, 'R10': 6, 'R5': 12, 'R2': 10, 'R1': 10}
total_in_till = sum(int(denomination[1:]) * count for denomination, count in till_float.items())

# Open the output file
with open('output.txt', 'w') as output_file:
    # Write header
    output_file.write("Till Start, Transaction Total, Paid, Change Total, Change Breakdown\n")
    
    # Process each transaction
    for line in lines:
        items, paid = line.strip().split(';')
        items = items.split(',')
        paid = int(paid.split('-')[0])  # Considering only the first payment
        
        # Calculate transaction total
        transaction_total = sum(int(item.split()[-1][1:]) for item in items)
        
        # Calculate change
        change_breakdown = calculate_change(paid, transaction_total)
        
        # Update till float
        for item in items:
            denomination = item.split()[-1]
            till_float[denomination] -= 1
        
        # Write to output file
        output_file.write(f"R{total_in_till}, R{transaction_total}, R{paid}, R{paid - transaction_total}, {'-'.join(change_breakdown)}\n")
        total_in_till += paid - transaction_total
        # do add anything else if there is a need

# Write till float at the end of the output file
with open('output.txt', 'a') as output_file:
    output_file.write(f"R{total_in_till}")
