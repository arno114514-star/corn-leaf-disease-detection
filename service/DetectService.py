import time
import os
from stu_django import settings
from ultralytics import YOLO

def img_detect(file):
    # 1.通过file对象，获取到文件名
    filename=file.name
    # 2.获取时间戳
    timestamp=int(time.time())
    # 3.字符串分割
    result=filename.split(".")
    new_name = str(timestamp)+"." +result[-1]
    # 4.保存图片
    save_path=os.path.join(settings.BASE_DIR,"static","images","detect",new_name)
    try:
        with open(save_path,"wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
            """
                检测代码
            """
            # 模型检测
            model_path=os.path.join(settings.BASE_DIR,"weights","best.pt")
            # 加载你们训练的模型
            model=YOLO(model_path)
            # 设置训练数据源
            results=model.predict(save_path,save=True)
            save_dir=""
            # 保存检测结果
            result_list=[]
            cls_names=[]
            for result in results:
                # 获取保存目录并转换为相对路径
                save_dir_str = str(result.save_dir)
                print('YOLO保存的原始路径:', save_dir_str)
                # 找到'runs'的位置，获取相对路径
                if 'runs' in save_dir_str:
                    runs_index = save_dir_str.index('runs')
                    # 从runs之后开始截取，去掉'runs/'前缀
                    relative_path = save_dir_str[runs_index + 5:]  # 5是'runs/'的长度
                else:
                    relative_path = save_dir_str
                # 使用正斜杠替换反斜杠
                relative_path = relative_path.replace('\\', '/')
                # 拼接文件名
                save_dir = relative_path + '/' + new_name
                print('最终返回的图片路径:', save_dir)
                for box in result.boxes:
                    cls_index=int(box.cls.item())
                    cls_name=result.names[cls_index]
                    conf=round(float(box.conf.item()),2)
                    cls_names.append(cls_name)
                    # 返回数据
                    result_list.append({"cls_name":cls_name,"conf":conf})
                
                # 检查是否检测到对象
                if len(cls_names) > 0:
                    print('检测结果图片路径:', save_dir)
                    return{
                        "status":200,
                        "msg":"检测完成",
                        "data":{
                            "resultImgUrl":save_dir,
                            "resultList":result_list,
                        }
                    }
                else:
                    return{
                        "status":500,
                        "msg":"未检测到目标"
                    }
            return{
                "status":200,
                "msg":"上传成功",
            }
    except Exception as e:
        print(e)
        return {
            "status":500,
            "msg":"上传失败"
        }