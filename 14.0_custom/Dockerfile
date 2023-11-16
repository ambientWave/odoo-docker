FROM odoo:14
user root
# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
COPY ./odoo.conf /etc/odoo/

# Set permissions and Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN chown root /etc/odoo/odoo.conf \
    && mkdir -p /mnt/extra-addons \
    && chown -R root /mnt/extra-addons
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose Odoo services
EXPOSE 8069 8071 8072

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

# COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Set default user when running the container
# USER odoo

# ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
