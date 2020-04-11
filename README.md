# ishop


# api

总的规则说明，所有请求的返回结果，都按照这种格式
```
{
    success: <bool>,    # 一般false的话表示有异常出现，客户端则会去显示message信息
    message: <string>
    ...
}
```


## account

### create_address
添加订单中的收货地址
```
req:
<string> shigongdanwei  # 施工单位
<string> project_name   # 项目名称
<string> project_address   # 项目地址
<string> project_contact   # 项目联系人
<string> shouhuoren   # 收货人
<string> shouhuoren_phone   # 收货人电话

resp:
<bool> result   # false的情况下，客户端显示message信息
```

### update_address
更新订单中的收货地址
```
req:
<int> address_id
<string> shigongdanwei  # 施工单位
<string> project_name   # 项目名称
<string> project_address   # 项目地址
<string> project_contact   # 项目联系人
<string> shouhuoren   # 收货人
<string> shouhuoren_phone   # 收货人电话

resp:
<bool> result   # false的情况下，客户端显示message信息
```

### delete_address
删除订单中的收货地址
```
req:
<int> address_id

resp:
<bool> result   # false的情况下，客户端显示message信息
```



## goods

### root_category
获取一级目录
```
req:

resp:
<list>  [{...}, {...}, ...] # list of category dict
    <dict>  # category dict
    {
        id: <int>,
        label: <string>,
        logo: <string>,
        is_new: <bool>,
        is_hot: <bool>
    }

```

### sub_category
获取一级目录对应的二三级目录，三级目录是品牌目录
```
req:
<int> cate_id

resp:
<list>  [{...}, {...}, ...]     # list of category dict
    <dict>  # category dict
    {
        id: <int>,
        label: <string>,
        logo: <string>,
        brand: <list>   # list of category dict
        [
            {
                id: <int>,
                label: <string>,
                logo: <string>,
            },...
        ]
    }

```

### goods_list
获取二级目录下所有商品，并按照三级目录默认选中
```
req:
<int> sub_cate_id
<int> brand_id

resp:
<list>  [{...}, {...}, ...]     # list of category dict
    <dict>  # category dict
    {
        id: <int>,
        label: <string>,
        logo: <string>,
        goods: <list>   # list of category dict
        [
            {
                id: <int>,
                name: <string>,
                main_img: <string>,
                min_price: <int>,   # 防止浮点数计算，直接用整数，客户端除于100后得到元
                max_price: <int>,
                short_desc: <string>
            },...
        ]
    }

```

### goods_detail
通过商品id获取商品详情
```
req:
<int> goods_id

resp:
<dict>  {...}
{
    id: <int>,
    cate: <string>,
    sub_cate: <string>,
    brand: <string>,
    name: <string>,
    main_img: <string>,
    short_desc: <string>,
    img_list: <string>,
    detail: <string:html>,
    count: <int>,
    min_price: <int>,   # 防止浮点数计算，直接用整数，客户端除于100后得到元
    max_price: <int>,
    is_new: <bool>,
    is_hot: <bool>,
    sold_count: <int>,
    guige: <list>,
    [
        {
            id: <int>,
            label: <string>,    # 例如颜色
            value: <string>     # 红/蓝/白
        },...
    ]
}

```

### new_goods_list
按照请求数量获取新上架商品列表
```
req:
<int> count

resp:
<list>  [{...}, {...}, ...] # list of goods dict
    <dict>  # goods dict
    {
        id: <int>,
        name: <string>,
        main_img: <string>,
        min_price: <int>,   # 防止浮点数计算，直接用整数，客户端除于100后得到元
        max_price: <int>,
        short_desc: <string>
    }

```

### hot_goods_list
按照请求数量获取畅销商品列表
```
req:
<int> count

resp:
<list>  [{...}, {...}, ...] # list of goods dict
    <dict>  # goods dict
    {
        id: <int>,
        name: <string>,
        min_price: <int>,   # 防止浮点数计算，直接用整数，客户端除于100后得到元
        max_price: <int>,
        short_desc: <string>
    }

```


## order

### add_to_cart
添加商品到购物车
```
req:
<int> goods_id
<string> guige_list # guige_id,value;guige_id,value;...
<int> count

resp:
<bool> result   # false可能是对应的规格库存不够，客户端显示message信息
```

### cart_gen_order
购物车中选中的商品列表生成订单
```
req:
<string> cart_list # cart_id,count;cart_id,count;...  购物车允许更新商品的数量，请求的时候带上最终填写的数量
<int> address_id

resp:
<bool> result   # false可能是对应的规格库存不够，客户端显示message信息
```