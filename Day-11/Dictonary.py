# student_info = {
#     "name": "sravan",
#     "id": "2203601",
#     "location": "Hyd",
#     "office": "synergy"
# }

# key_to_print = ["name", "id", "location"]
# for key in key_to_print:
#     print(student_info[key])


ec2_info =[
    {
        "instance_name": "sravan_ec2",
        "type": "t2.mirco",
        "tier": "free"
    },
    {
        "instance_name": "kumar",
        "type": "t2.medium",
        "tier": "2USD"

    },
    {
        "instance_name": "sai",
        "type": "t2.large",
        "tier": "3USD"
    }
]

key_to_print_ec2 = ["instance_name", "type", "tier"]

for key in key_to_print_ec2:

    print(f"{key}: {ec2_info[0][key]}")

