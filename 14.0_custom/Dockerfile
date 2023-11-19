FROM odoo:14
RUN whoami

# RUN mkdir -p /mnt/extra-addons
ADD ./custom/base_synchro /mnt/extra-addons/base_synchro
# RUN chattr -V -ais /mnt/extra-addons \
#     && chown -R odoo /mnt/extra-addons
    

# VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]



CMD odoo --limit-time-real 9999999 --limit-time-cpu 9999999 --database=sync14_0_p40t  --db_user=sync14_0_p40t_user --db_password=D1nwskO9BEdGfNbrn9CzFFRU5sFLPxVw --db_host=dpg-clcv3avgsrdc73fhlkeg-a --db_port=5432 -i all
