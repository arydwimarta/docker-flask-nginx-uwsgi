#use nginx image
FROM nginx

#remove default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

#replace with our nginx configuration
COPY nginx.conf /etc/nginx/conf.d/