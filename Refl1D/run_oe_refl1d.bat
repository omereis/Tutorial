docker rm -f oe_refl1d
docker build --rm -f Refl1D.docker -t oe_refl1d .
docker run -it -d --name oe_refl1d oe_refl1d
docker exec -it oe_refl1d bash

<!--
			<div id="" class="ui-layout-resizer ui-layout-resizer-south ui-layout-resizer-open ui-layout-resizer-south-open" title="Resize" aria-disabled="false"
			style="position: absolute; padding: 0px; margin: 0px; font-size: 1px; text-align: left; overflow: hidden; z-index: 2; cursor: s-resize;
				bottom: 138px; width: 506px; height: 6px; left: 10px;">

			<div id="" class="ui-layout-toggler ui-layout-toggler-south ui-layout-toggler-open ui-layout-toggler-south-open" title="Closer"
				style="position: absolute; display: block; padding: 0px; margin: 0px; overflow: hidden; text-align: center; font-size: 1px;
				cursor: pointer; z-index: 1; visibility: visible; width: 48px; height: 6px; left: 228px; top: 0px;">
			</div>

		</div>
	</div>

	<div id="" class="ui-layout-resizer ui-layout-resizer-west ui-layout-resizer-open ui-layout-resizer-west-open" title="Resize" aria-disabled="false"
		style="position: absolute; padding: 0px; margin: 0px; font-size: 1px; text-align: left; overflow: hidden; z-index: 2; cursor: w-resize;
			left: 200px; height: 1014px; width: 6px; top: 0px;">
		<div id="" class="ui-layout-toggler ui-layout-toggler-west ui-layout-toggler-open ui-layout-toggler-west-open" title="Close"
			style="position: absolute; display: block; padding: 0px; margin: 0px; overflow: hidden; text-align: center;
				font-size: 1px; cursor: pointer; z-index: 1; visibility: visible; height: 48px; width: 6px; top: 482px; left: 0px;">
		</div>
	</div>
-->
