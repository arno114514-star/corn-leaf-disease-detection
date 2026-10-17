# 玉米叶病检测系统

基于YOLO深度学习模型的玉米叶片病害检测系统，采用Django框架开发，提供Web界面进行图片上传和病害识别。

## 项目简介

本系统利用训练好的YOLO模型，能够自动识别玉米叶片中的常见病害类型（如普通锈病等），并通过Web界面展示检测结果和标注图片。

## 技术栈

### 后端
- **Django 6.0.5** - Web框架
- **Ultralytics YOLO** - 目标检测模型
- **SQLite** - 数据库

### 前端
- **Vue.js** - 前端框架
- **Element UI** - UI组件库
- **Axios** - HTTP请求库
- **Font Awesome** - 图标库

### 其他
- **Python** - 编程语言
- **Anaconda** - Python环境管理

## 项目结构

```
stu_django/
├── controller/              # 控制器层
│   ├── PageController.py   # 页面路由控制
│   └── SystemController.py # 业务逻辑控制
├── service/                 # 服务层
│   ├── DetectService.py    # 检测服务
│   └── UserService.py      # 用户服务
├── templates/               # 前端模板
│   ├── login.html          # 登录页面
│   ├── system.html         # 系统主页面
│   └── imgDetect.html      # 图片检测页面
├── static/                  # 静态资源
│   ├── images/             # 图片资源
│   │   ├── detect/         # 检测结果图片
│   │   └── yumiwang.png    # 背景图片
│   ├── css/                # 样式文件
│   ├── js/                 # JavaScript文件
│   ├── axios/              # Axios库
│   └── element-ui/         # Element UI库
├── weights/                 # 模型权重
│   └── best.pt             # YOLO训练模型
├── runs/                    # YOLO检测结果输出目录
├── stu_django/              # Django项目配置
│   ├── settings.py         # 项目配置
│   └── urls.py             # URL路由配置
└── manage.py               # Django管理脚本
```

## 功能特性

- ✅ 用户登录认证
- ✅ 图片上传功能
- ✅ YOLO模型自动检测
- ✅ 检测结果可视化展示
- ✅ 病害类型和置信度显示
- ✅ 响应式Web界面

## 安装与运行

### 环境要求

- Python 3.8+
- Anaconda（推荐）

### 安装步骤

1. **克隆或下载项目**
   ```bash
   cd E:\实训\stu_django
   ```

2. **创建并激活虚拟环境**
   ```bash
   conda create -n yoloLu_env python=3.x
   conda activate yoloLu_env
   ```

3. **安装依赖**
   ```bash
   pip install django
   pip install ultralytics
   pip install django-cors-headers
   pip install pillow
   ```

4. **准备模型文件**
   - 确保 `weights/best.pt` 文件存在
   - 这是训练好的YOLO模型权重文件

5. **运行项目**
   ```bash
   python manage.py runserver 8000
   ```

6. **访问系统**
   - 打开浏览器访问：`http://127.0.0.1:8000/`
   - 默认会自动跳转到登录页面

## 使用说明

### 登录系统

1. 访问首页会自动跳转到登录页面
2. 输入用户名和密码
3. 点击 "Login" 按钮登录

### 图片检测

1. 登录后进入系统主页面
2. 在左侧菜单选择 "图像检测"
3. 点击 "选取文件" 按钮选择要检测的图片
4. 点击 "执行检测" 按钮开始检测
5. 等待检测完成，查看结果：
   - 左侧显示原图
   - 右侧显示检测结果（带标注框）
   - 下方显示检测到的病害类型和置信度

## 配置说明

### 数据库迁移

首次运行前需要执行数据库迁移：

```bash
python manage.py migrate
```

### 媒体文件配置

在 `stu_django/settings.py` 中配置：

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'runs'
```

检测结果图片保存在 `runs/detect/` 目录下。

### CORS配置

已配置跨域支持，允许本地访问：

```python
CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:8000"]
```

## 常见问题

### 1. 图片无法显示

- 检查浏览器控制台是否有404错误
- 确认 `MEDIA_ROOT` 配置正确
- 清除浏览器缓存（Ctrl + F5）

### 2. 检测结果路径问题

系统会自动处理Windows和Linux的路径差异，确保URL使用正斜杠 `/`。

### 3. 浏览器自动填充黄色背景

已通过CSS修复，如果仍看到黄色背景，请清除浏览器保存的密码后重试。

### 4. 端口被占用

如果8000端口被占用，可以更换端口：

```bash
python manage.py runserver 8080
```

## 开发说明

### 添加新的检测功能

1. 在 `service/DetectService.py` 中添加新的检测方法
2. 在 `controller/SystemController.py` 中添加对应的视图函数
3. 在 `stu_django/urls.py` 中配置URL路由
4. 创建对应的前端页面

### 修改页面标题

- 登录页面：编辑 `templates/login.html` 第20行
- 系统主页：编辑 `templates/system.html` 第58行

### 更换背景图片

- 登录页面：修改 `static/css/login.css` 第14行
- 系统主页：修改 `templates/system.html` 中的 `.el-main` 样式

## 项目维护

### 清理检测结果

定期清理 `runs/detect/` 目录下的旧检测结果：

```bash
# Windows PowerShell
Remove-Item -Recurse -Force runs\detect\*

# Linux/Mac
rm -rf runs/detect/*
```

### 更新模型

将新的模型文件替换 `weights/best.pt` 即可。

## 许可证

本项目仅供学习和研究使用。

## 联系方式

如有问题或建议，请联系项目维护者。

---

**最后更新**: 2026年5月15日
