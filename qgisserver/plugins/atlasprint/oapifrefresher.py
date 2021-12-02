"""
***************************************************************************
    QGIS Server Plugin Filters: Add a new request to print a specific atlas
    feature
    ---------------------
    Date                 : November 2021
    Copyright            : (C) 2021 by Yverdon-les-Bains
    Email                : sit at ylb dot ch
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.core import (
    QgsProject,
    QgsCoordinateReferenceSystem,
    QgsDataProvider,
)

from .logger import Logger


__copyright__ = "Copyright Yverdon-les-Bains"
__license__ = "GPL version 3"
__email__ = "sit@ylb.ch"


class OAPIFRefresher:
    def refresh_geocity_oapif_layers_for_current_atlas_feature(id):

        project = QgsProject.instance()
        for layer in QgsProject.instance().mapLayers().values():
            uri = layer.dataProvider().uri()
            # refresh and filter OAPIF virtual layer
            if layer.dataProvider().name() == "OAPIF" and layer.isValid():
                # only for geocity endpoints
                if uri.param("typename") in [
                    "permits",
                    # TODO: refresh empty point/line/poly layers
                    # "permits_poly",
                    # "permits_line",
                    # "permits_point",
                ]:

                    # replace url in order to filter for the required feature only
                    uri.removeParam("url")
                    uri.setParam("url", f"http://web:9000/wfs3/?permit_request_id={id}")
                    Logger().info(
                        "qgis-printatlas - uri: " + uri.uri(expandAuthConfig=False)
                    )

                    layer.setDataSource(
                        uri.uri(expandAuthConfig=False),
                        uri.param("typename"),
                        "OAPIF",
                        QgsDataProvider.ProviderOptions(),
                    )
                    layer.dataProvider().updateExtents()
                    layer.dataProvider().reloadData()
                    layer.updateFields()
                    layer.triggerRepaint()
                    Logger().info(
                        "qgis-printatlas - refreshed data source: "
                        + uri.param("typename")
                    )
                    Logger().info(
                        "qgis-printatlas - uri: " + uri.uri(expandAuthConfig=False)
                    )

            # refresh virtual layers
            if layer.dataProvider().name() == "virtual" and layer.isValid():
                layer.dataProvider().updateExtents()
                layer.dataProvider().reloadData()
                layer.updateFields()
                layer.triggerRepaint()
                Logger().info(
                    "qgis-printatlas - refreshed virtual layer: "
                    + uri.param("typename")
                )
