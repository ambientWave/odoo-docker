FROM odoo:14
RUN whoami

# RUN mkdir -p /mnt/extra-addons
ADD ./custom/base_synchro /mnt/extra-addons/base_synchro
# RUN chattr -V -ais /mnt/extra-addons \
#     && chown -R odoo /mnt/extra-addons
    

# VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]



CMD odoo --limit-time-real 9999999 --limit-time-cpu 9999999 --database=odoo_14_0_remote_fresh  --db_user=odoo_14_0_remote_fresh_user --db_password=YFJC2wIfEHadzQRQD0NPf8zQqcrr9XhH --db_host=dpg-claneam16hkc739crt00-a --db_port=5432 -i all
