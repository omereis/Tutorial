docker rm -f oe_refl1d
docker build --rm -f Refl1D.docker -t oe_refl1d .
docker run -it -d --name oe_refl1d oe_refl1d
docker exec -it oe_refl1d bash

<script src="//www.ncnr.nist.gov/instruments/magik/d3-science-v4/lib/heat-chart.js"></script>
<script src="./embed_src/heat-chart.js"></script>