#!/bin/bash

# Update the system and install necessary packages
yum update -y
yum install -y httpd

# Start the Apache server
systemctl start httpd
systemctl enable httpd


# ---------------------------------------------------------
# Get EC2 instance metadata using IMDSv2
# ---------------------------------------------------------

TOKEN=$(curl -sX PUT \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" \
  http://169.254.169.254/latest/api/token)

INSTANCE_ID=$(curl -s \
  -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/instance-id)

AVAILABILITY_ZONE=$(curl -s \
  -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/placement/availability-zone)

# ---------------------------------------------------------
# Create the index.html file
# ---------------------------------------------------------

cat > /var/www/html/index.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>EC2 Instance</title>
</head>

<body style="font-family:Arial; background:#f4f6f8;">

<div style="max-width:600px; margin:50px auto; background:#fff; padding:30px; border-radius:8px; text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.1);">

    <h2 style="color:#2c3e50; margin-bottom:25px;">
        🌟 Daily Motivation for my Agentic AI Students.. - Subrat
    </h2>

    <p style="font-size:18px; color:#555; font-style:italic;">
        "Success is the sum of small efforts, repeated day in and day out."
    </p>

    <p style="color:#777; margin-bottom:30px;">
        — Robert Collier
    </p>

    <hr style="border:none; border-top:1px solid #ddd; margin:25px 0;">

    <p style="font-size:18px; color:#555; font-style:italic;">
        "The future depends on what you do today."
    </p>

    <p style="color:#777;">
        — Mahatma Gandhi
    </p>

    <hr style="border:none; border-top:1px solid #ddd; margin:25px 0;">

    <h3 style="color:#2c3e50;">EC2 Instance Details</h3>

    <p>
        <strong>Instance ID:</strong><br>
        $INSTANCE_ID
    </p>

    <p>
        <strong>Availability Zone:</strong><br>
        $AVAILABILITY_ZONE
    </p>

</div>

</body>
</html>
EOF


# Check the httpd service is correctly set up
systemctl enable httpd
systemctl restart httpd