#
#data_iiiq = {}
#data_iiq = {}
#data_iq = {}
#
#    inner_queryset = Data.objects.filter(parent=None)
#
#        for iq in inner_queryset:
#            data_iq[q.name] = inner_queryset
#                inner_inner_queryset = Data.objects.filter(parent=iq)
#                for iiq in inner_inner_queryset:#data_iiq
#                    inner_inner_inner_queryset = Data.objects.filter(parent=iiq)
#                    for iiiq in inner_inner_inner_queryset:#data_iiiq
#                    data_iiiq[iiq.name] = inner_inner_inner_queryset
#        data_iiq[iq.name] = data_iiiq