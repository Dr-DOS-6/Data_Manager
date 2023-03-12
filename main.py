stat = 0
count =0
var_list = []
appendcount = int(input("How many datas will you enter? "))
while stat == 0:
  exectxt = f'{str(count+1)}つ目のデータを入力してください。'
  if len(var_list) == appendcount:
    stat = int(input("データ入力を終了しますか？ 0:続ける 1:終了 "))
    if stat == 0:
      appendcount += int(input("いくつのデータを入力しますか？ "))
  var_list.append(None)
  var_list[count] = f"var{str(count+1)}"
  var_name=var_list[count]
  if stat ==0:
    exec("{} = input(exectxt)".format(var_name))
  else:
    pass
  count +=1
with open('data.txt','w') as f:
      for i in range(len(var_list)):
        f.write(f'{i},{exectxt}')
with open('data.txt','r') as f:
    print(f.read())