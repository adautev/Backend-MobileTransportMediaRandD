#!/usr/bin/env bash
apt-get update
apt-get install -y python python3 python3-virtualenv python3-pip git
mkdir /var/www
cd /var/www
mkdir /root/.ssh
touch /root/.ssh/id_rsa
touch /root/.ssh/id_rsa.pub
#Don't judge me for /root. It's a PoC! :D
cat <<EOT >> /root/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2i5VhA9fjycJO4PlpT9VB48fHSOG8pITe7e5G3NIJHOmUH22
bNTGupUdAY9jYZkZtqGm/EF1DxkQInWK3fA47rvese0419LAuekJs1E65Ijjpz/5
bLJqS9LdJOe9/QrIPZe/I6Jq3jbR72VkjppZQiMXC2y7IYNEWCX0Ju0mDVMGfm0F
bTcje9pEiZMohhzxIwiytAYSZLnUe/M7P6mRlqhn9PBCLSweMDPUWG40+tl8ZQox
ocS6I596R2ZBgYVMiKUZlxcmomMea1mP1TuKUrcZWBNzMOCXactGgrRTW+vNZpw0
wuAEPwg1KAVFy1BR2Dp+Fj1zMF4uXyMl8GQ/XQIDAQABAoIBAQC+wkwajqZqLyMv
Wf7rIBhj54q4m1tdssI+JUA+8+hblpIPRhq9xLuMXtthhdDKgGWu/F9XppOGg89L
kaG8sk/Uy4XF4zcT3DyNT2cf1SG8tsL0dEbL9qJhcRfRMJ04JLk2wPppWZQ+fYfH
28qzs9fer3dykbp7bp3OxEBX2HiwpA1/AACdBnoQl7bZwySvf5hrh2Wra3HHRqt/
rPR5Gxb7KM88KFD9jOVXLX2PaezOkHTiv9oCau/xP8KyiveZ5nquSwCmt2tsIfCc
VyBUlQnYksYqlPRHuncwRvQPz7YMHdBjzmG0YSbWi+y9RVfpLFQXOBxM+GKf/Ky4
c3sbHk4BAoGBAO2au6XqUstoPU7Qc0k3XNtLT8TA50j0zVCvzECCNwzI71uzW1YX
8rh9tY6w4LfxeCloJDgsEMKoodx09M3cIpr1QkAfZKBSdXhWH95BHEnoPAE90Xul
hIiyQbxl8Nxg1fB63H4rB7mPfdrao4ckJI4ZQVR7+m87Fr2w4vDGGg09AoGBAOsS
ogYUuOLdpy85ltPgV8qXp/uJbVLsZHOdJl8FpcWhB115krgNcSQzQgtEMWqy7uZI
c/kOdXY4Po82FWhCKEDcXPmFK/KTa6KNWrvfns2NgUPl4dOsrS2aeD0vEHZESPiq
xqPxBouFw49/m4QUN8So0AIRQr/MCUg74F5GQFyhAoGAaUugCufr5w571NiVroWl
Vd1rLUNbe75Y2n/9oTzTjovhXx79xAp62v2CnwiNnZaZ7KelHWuRxeIbUOpXrn72
qvszb905p77DJh/soX7zPWF4bghqNERmlnmAnjAC7HbReG/KFPOWycnoOTuZKoN+
26YfiIQkuHRUIJ4qBA+WbfUCgYAvOJ39lLoTMK196hanV0CrfM2M1O12I/CF3QKx
QeQsEA33tA1KFcEtoXJZ6wf2RB2Devh5BnOIHQJMKHQibm/Bn8K5iQvr/bs4eybH
6MLwzcUyy4IS0HQ1XftbZxHqgAsckMm4cxl6e5NuRxcJcDpHshWe5LLA7o7KyORo
a7pQIQKBgQC0LGE8t6gx06j8ZbItAQLAHP7z2g9Yz+RLSufVFoTf2rP7N08jN5Hv
jkOOMsrWjKHHuSffOD/sCPxz6/XeqgUDe7Mpc9NQeLgJJRPWzL6yPme8hB1zQujy
rX2kwMKGCzey8KWhlpL5cHVWUjvML/vBUzyxW8lzKuuzJKzvXWPpWg==
-----END RSA PRIVATE KEY-----
EOT
cat <<EOT >> /root/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDaLlWED1+PJwk7g+WlP1UHjx8dI4bykhN7t7kbc0gkc6ZQfbZs1Ma6lR0Bj2NhmRm2oab8QXUPGRAidYrd8Djuu96x7TjX0sC56QmzUTrkiOOnP/lssmpL0t0k5739Csg9l78jomreNtHvZWSOmllCIxcLbLshg0RYJfQm7SYNUwZ+bQVtNyN72kSJkyiGHPEjCLK0BhJkudR78zs/qZGWqGf08EItLB4wM9RYbjT62XxlCjGhxLojn3pHZkGBhUyIpRmXFyaiYx5rWY/VO4pStxlYE3Mw4Jdpy0aCtFNb681mnDTC4AQ/CDUoBUXLUFHYOn4WPXMwXi5fIyXwZD9d
EOT
chmod 600 /root/.ssh/*
git clone git@github.com:adautev/MobileTransportMediaRandD-BackEnd.git
cd /var/www/MobileTransportMediaRandD-BackEnd
alias python=python3
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
mv dal/config_example.py dal/config.py
sed -i 's/ConfigExample/Config/g' dal/config.py
export DATABASE_URL="postgresql://adautev:adiadi@192.168.0.119:7010/adautev"
export FLASK_APP=/var/www/MobileTransportMediaRandD-BackEnd/main.py
#i am too lazy to set up migrations + pki generation. (: