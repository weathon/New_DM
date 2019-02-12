import eel


@eel.expose
def helloworld(a, b):
    print(a, b, a + b)
    return [
                {
                    id: 1,
                    label: "安徽省",
                    children: [
                        {
                            id: 2,
                            label: "马鞍山市",
                            disabled: true,
                            children: [
                                {
                                    id: 3,
                                    label: "和县",
                                },
                                {
                                    id: 4,
                                    label: "花山区",
                                }
                            ]
                        }
                    ]
                },
                {
                    id: 5,
                    label: "河南省",
                    children: [
                        {
                            id: 6,
                            label: "郑州市"
                        }
                    ]
                }
            ]

eel.init('./')
eel.start('index.html')
