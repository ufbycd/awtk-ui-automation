# awtk-ui-automation

AWTK UI 自动化测试代理(试验阶段...)。

## 准备

1. 获取 awtk 并编译

```
git clone https://github.com/zlgopen/awtk.git
cd awtk; scons; cd -
```

2. 获取 awtk-restful-httpd 并编译
```
git clone https://github.com/zlgopen/awtk-restful-httpd.git
cd awtk-restful-httpd; scons; cd -
```

3. 获取 awtk-ui-automation 并编译
```
git clone https://github.com/zlgopen/awtk-ui-automation.git
cd awtk-ui-automation; scons
```

## 运行

> 考虑到 github 的下载速度，生成的临时资源没放到 git 中，需要自己生成资源：

```
./scripts/update_res.py all
```

```
./bin/demo
```

