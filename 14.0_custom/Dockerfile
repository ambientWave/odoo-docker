FROM odoo:14
RUN whoami

# RUN mkdir -p /mnt/extra-addons
ADD ./custom/base_synchro /mnt/extra-addons/base_synchro
# RUN chattr -V -ais /mnt/extra-addons \
#     && chown -R odoo /mnt/extra-addons
    

# VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]



CMD odoo --limit-time-real 9999999 --limit-time-cpu 9999999 --database=ice_14_0  --db_user=ice_14_0_user --db_password=QVLtVYWNRmbN7wGNyWE5SHyRGZshNat1 --db_host=dpg-clata9ug1b2c73a862pg-a --db_port=5432 -i all
