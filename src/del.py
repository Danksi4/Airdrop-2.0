import subprocess

# Run the ifconfig command
result = subprocess.run(['ifconfig'], capture_output=True, text=True)
result = result.stdout
# Print the output
print(result)