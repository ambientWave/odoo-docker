FROM odoo:14
RUN echo $USER

RUN mkdir -p /mnt/extra-addons
ADD ./custom/base_synchro /mnt/extra-addons/base_synchro
RUN chattr -i /mnt/extra-addons \
    && chown -R root /mnt/extra-addons
    

VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]



CMD odoo --database=odoo_14_0_remote  --db_user=odoo_14_0_remote_user --db_password=Dyk5vsn7Gs6z1XdG81QSWOTHHbiq9PYU --db_host=dpg-clah11f8im3c73d9b7m0-a --db_port=5432 -i ir_attachment
