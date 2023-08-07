# Input - 34.34, 12.01, 17.42, 4.93
# Output_dollars - 68
# Outputs_cents - 70
price_1 = 34.34
price_2 = 12.01
price_3 = 17.42
price_4 = 4.93

sum = price_1 + price_2 + price_3 + price_4

print(f'Output_dollars {int(sum)}')
print(f'Output_cents {int((sum - int(sum)) * 100)}')