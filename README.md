# Deploy Selenium Grid on OpenShift

## Deploy by images:
```
oc new-project selenium-grid

oc new-app --docker-image=selenium/hub:3.5.3-astatine

oc new-app -e HUB_PORT_4444_TCP_ADDR=hub -e HUB_PORT_4444_TCP_PORT=4444 --docker-image=selenium/node-chrome:3.5.3-astatine

oc new-app -e HUB_PORT_4444_TCP_ADDR=hub -e HUB_PORT_4444_TCP_PORT=4444 --docker-image=selenium/node-firefox:3.5.3-astatine
```
change the type of service **hub** to **NodePort**

## Deploy by template:

```
oc create -f selenium-grid.yaml
```