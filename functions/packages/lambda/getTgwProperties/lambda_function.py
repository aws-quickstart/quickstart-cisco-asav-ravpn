import json
import logging
import boto3
import cfnresponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_vpn_attachment_ids(vpn_id, stackName):
    try:
      myDict = {}
      client = boto3.client('ec2')
      vpn = client.describe_vpn_connections(VpnConnectionIds=[vpn_id])['VpnConnections']
      tgw = client.describe_transit_gateway_attachments()['TransitGatewayAttachments']
      rtb = client.describe_transit_gateway_route_tables()["TransitGatewayRouteTables"]
      logger.info(vpn)
      for index in range(len(vpn)):
        mylist = []
        for vgwTelemetry in vpn[index]['VgwTelemetry']:
          mylist.append(vgwTelemetry['OutsideIpAddress'])
        myDict['vpn'+str(index)+'OutsideIps']=mylist
      #Get vpn tgw attachment ids
      for dictionary in tgw:
        if dictionary["ResourceId"] == vpn_id:
          myDict["vpn1_tgw_attachment_id"] = dictionary['TransitGatewayAttachmentId']
      #Get rtb ids
      for dictionary in rtb:
        if dictionary["Tags"]:
          for tagsdictionary in dictionary["Tags"]:
            if stackName+"-Securityrtb" in tagsdictionary['Value']:
              myDict["security_tgw_rtb_id"] = dictionary['TransitGatewayRouteTableId']
    except Exception as e:
      logger.info('get vpn tgw attachment id failure: {}'.format(e))

    return myDict

def lambda_handler(event, context):
    # This comment was added to force an update on this function's code
    logger.info('got event {}'.format(event))
    responseData = {}
    
    if event['RequestType'] == 'Create':
      responseData = get_vpn_attachment_ids(event['ResourceProperties']['vpn_id'],event['ResourceProperties']['stackName'])
    
    else: # delete / update
      rs = event['PhysicalResourceId'] 
      responseData['TransitGatewayAttributes'] = rs
    
    logger.info('responseData {}'.format(responseData))
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
