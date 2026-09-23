# shixisheng · 实习生信息管理系统

> 一个 Django 写的实习生 CRUD 小系统：新增、编辑、删除、列表，后台兼 Bootstrap 前台模板。

**维护状态**：早期练手项目，已归档。

---

## 一、这是个什么项目

用 Django 实现的一套最朴素的**人员信息增删改查**：

- 列表页看所有实习生
- 表单页新增 / 编辑
- 点删除按 id 删掉一条
- 图片单独走 `Image` 模型管理

前台套了一套 Bootstrap 风格的网页模板（含 `windows8_site_ltr.css`、`bootstrap.css` 等），
所以它是"后端 CRUD + 现成模板皮肤"的组合，重点在功能不在设计。

## 二、路由一览

| 路由 | 视图 | 说明 |
|---|---|---|
| `/` | `home` | 首页，列出全部实习生 |
| `/hello/<name>` | `hello` | 按名称取参的演示视图 |
| `/new` | `new` | 新增页面 |
| `/delete/<id>` | `delete` | 按 id 删除 |
| `/edit/<id>` | `edit` | 编辑页（带回填） |
| `/edit_view/<id>` | `edit_view` | 编辑提交处理 |
| `/admin/` | Admin | 后台管理 |
| `/media/<path>` | static.serve | 开发环境媒体直出 |

## 三、数据模型

| 模型 | 字段 |
|---|---|
| `Image` | `img`（ImageField） |
| `student` | `name`（姓名） · `addrss`（地址，原样保留了拼写） · `count`（计数） · `date`（日期，`auto_now`） · `content`（备注） |

## 四、技术栈

| 项 | 说明 |
|---|---|
| 语言 | Python **2.7**（已 EOL） |
| 框架 | Django **1.7 / 1.8** |
| 数据库 | SQLite（`db.sqlite3`） |
| 前端 | Bootstrap 2.x + 现成网页模板（`static/css/`） |
| 后台 | Admin + `bootstrap_admin` |

## 五、目录结构

```
shixisheng/
├── manage.py
├── db.sqlite3
├── img/                        早期素材图（含多份重复产物）
├── media/img/                  后台上传
└── shixisheng/
    ├── settings.py             配置（含 SECRET_KEY）
    ├── urls.py                 CRUD 路由
    ├── models.py               Image / student
    ├── views.py                home / hello / new / delete / edit / edit_view
    ├── admin.py
    ├── templates/              列表页 / 表单页
    └── static/
        ├── css/                bootstrap、demo、style、windows8 站点样式
        └── images/             模板自带配图
```

## 六、本地运行

```bash
pyenv local 2.7.18
pip install "Django<1.9" Pillow bootstrap-admin

python manage.py runserver 0.0.0.0:8000
```

首页 `http://127.0.0.1:8000/`，建议先 `/admin` 建一条学生记录再看列表效果。

## 七、已知问题

- 删除 / 编辑都没有做权限与幂等控制，纯功能演示
- `settings.py` 里 `SECRET_KEY` 明文且已公开；`DEBUG = True`
- `img/` 与 `media/` 下有若干重复图片（不同后缀，是当年反复上传留下的），可以安全清理
- 模板依赖 Bootstrap 2.x，用现代浏览器打开会有样式错位

## 八、许可

早期学习作品，代码可随意参考；`static/` 下的网页模板素材版权归原模板作者，请勿商用。

---

## 免费赞助

这套东西是白送的：**不收费、不锁功能、不塞广告**。如果它帮你省了时间、或者多赚了钱，
可以扫码请 Emperor 喝杯茶 —— 完全自愿，不打赏也照样用、照样更新。

<p align="center">
  <img src="assets/sponsor-qr.png" alt="免费赞助 · Emperor、| 说事-不闲聊" width="280">
</p>

<p align="center"><sub>扫码可备注一句你在做什么类目，方便后续针对性更新</sub></p>
