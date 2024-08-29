#-----
#리스트 복사 메서드: copy()
#-----
datas=[11,22,33]
nums=datas
print(f'datas: {datas}\nnums:{nums}')

nums[0]='백'
print(f'datas: {datas}\nnums:{nums}')

datas=[11,22,33]
nums2=datas.copy()
print(f'datas: {datas}\nnums2:{nums2}')

nums2[0]='A'
print(f'datas: {datas}\nnums2:{nums2}')